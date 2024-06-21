#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""
from model_state import Base, State
import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys


def main():
    username, password, database = sys.argv[1:]
    engine = sql.create_engine(
        "mysql://{}:{}@localhost:\
        3306/{}".format(
            username, password, database
        )
    )
    session = sessionmaker(bind=engine)()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)


if __name__ == "__main__":
    main()
