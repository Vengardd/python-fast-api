from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import add_connection, find_connections
from database import get_db
from schemas import NewConnection, FindConnectionRequest

router = APIRouter()


@router.post("/api/addConnection")
def add_connection_api(connection_info: NewConnection, session: Session = Depends(get_db)):
    try:
        new_connection = add_connection(session, connection_info)
        return new_connection
    except Exception as ex:
        raise HTTPException(**ex.__dict__)


@router.post("/api/findConnection")
def find_connection_api(find_connection_request: FindConnectionRequest, session: Session = Depends(get_db)):
    try:
        connections_found = find_connections(session, find_connection_request)
        return str(connections_found) + " km"
    except Exception as ex:
        raise HTTPException(**ex.__dict__)
