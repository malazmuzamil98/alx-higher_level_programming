#!/usr/bin/python3
"""module for class state"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """database"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name


engine = create_engine('mysql://root:root@localhost:3306/hbtn_0e_4_usa')
