from sqlalchemy import Column, ForeignKey, Integer, String
from . import BaseModel

class User(BaseModel):
    __tablename__ = 'user'

    id = Column(String, primary_key=True)
    name = Column(String)

