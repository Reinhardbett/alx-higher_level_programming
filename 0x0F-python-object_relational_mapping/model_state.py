#!/usr/bin/python3
''' Create first sqlalchemy state model'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State class
    Attributes:
    __tablename__ (str): Table name
    id (int): State id
    name (str): The state name
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
