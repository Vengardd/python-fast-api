from queue import Queue, PriorityQueue
from sqlalchemy.orm import Session
from exceptions import ConnectionAlreadyExists, ConnectionNotFound
from models import Connection
from schemas import NewConnection, FindConnectionRequest


def add_connection(session: Session, connection_info: NewConnection):
    connection = session.query(Connection).filter(Connection.from_city_name == connection_info.from_city_name,
                                                  Connection.to_city_name == connection_info.to_city_name).first()
    if connection is not None:
        raise ConnectionAlreadyExists
    if connection_info.from_city_name == connection_info.to_city_name or not connection_info.from_city_name \
            or not connection_info.to_city_name or not connection_info.distance:
        raise ConnectionError
    new_connection = Connection(**connection_info.dict())
    session.add(new_connection)
    session.commit()
    session.refresh(new_connection)
    return new_connection


def find_connections(session: Session, find_connection_request: FindConnectionRequest):
    all_connections = get_graph_of_connections(session, find_connection_request)
    if find_connection_request.to_city not in map(lambda con: con[0], all_connections):
        raise ConnectionNotFound
    djikstra = search_for_path_djikstra(all_connections, find_connection_request)
    return djikstra[find_connection_request.to_city]


def get_graph_of_connections(session: Session, find_connection_request: FindConnectionRequest):
    queue = Queue()
    queue.put(find_connection_request.from_city)
    list_of_cities = []
    all_connections = []
    while not queue.empty():
        current_city = queue.get()
        connections = session.query(Connection).filter(Connection.from_city_name == current_city).all()
        for connection in connections:
            if connection.to_city_name not in list_of_cities:
                queue.put(connection.to_city_name)
                list_of_cities.append(connection.to_city_name)
        all_connections.append((current_city, connections))
    return all_connections


def search_for_path_djikstra(all_connections, find_connection_request):
    djikstra = {v: float('inf') for v in map(lambda con: con[0], all_connections)}
    djikstra[find_connection_request.from_city] = 0
    visited = []
    pq = PriorityQueue()
    pq.put((0, find_connection_request.from_city))
    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.append(current_vertex)
        current_vertex_connections = [x[1] for x in all_connections if x[0] == current_vertex][0]

        for city in map(lambda con: con[0], all_connections):
            connection_from_current_to_city = [x for x in current_vertex_connections if x.to_city_name == city]
            if connection_from_current_to_city:
                distance = connection_from_current_to_city[0].distance
                if connection_from_current_to_city[0].to_city_name not in visited:
                    old_cost = djikstra[city]
                    new_cost = djikstra[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, city))
                        djikstra[city] = new_cost
    return djikstra
