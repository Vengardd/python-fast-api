from pydantic import BaseModel

# TO support creation and update APIs
class NewConnection(BaseModel):
    from_city_name: str
    to_city_name: str
    distance: int

class FindConnectionRequest(BaseModel):
    from_city: str
    to_city: str
