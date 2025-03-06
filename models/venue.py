from pydantic import BaseModel

class Venue(BaseModel):

    name: str
    title: str
    study: str
