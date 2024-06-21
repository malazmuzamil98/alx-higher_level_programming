#!/usr/bin/python3
"""
module for class that mange databases
"""
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """databases class  to manage the state of a device."""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'), nullable=False)

    def __init__(self, name, state_id):
        self.name = name
        self.state_id = state_id


engine = create_engine('mysql://root:root@localhost:3306/hbtn_0e_4_usa')