from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from database import Base


class Connection(Base):
    __tablename__ = "connection"

    id = Column(Integer, primary_key=True, index=True)
    from_city_name = Column(String(100), index=True)
    to_city_name = Column(String(100), index=True)
    distance = Column(Integer)

    def __repr__(self):
        return "ID: " + str(
            self.id) + ", fromCity: " + self.from_city_name + ", toCityName: " + self.to_city_name + ", distance: " + str(
            self.distance)
