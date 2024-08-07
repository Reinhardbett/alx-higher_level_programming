#!/usr/bin/python3
"""Realationship city table"""


from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """ City class
    __tablename__: its thetable of the class City
    id (int): the id of the class City
    name (str): the name of the class City
    state_id (int): Its the id of the state of the class City
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
