#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""
from model_state import Base, State
import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base
import sys


def main():
    username, password, database, state_name = sys.argv[1:]
    engine = sql.create_engine(
        "mysql://{}:{}@localhost:\
        3306/{}".format(
            username, password, database
        )
    )
    Base.metadata.create_all(engine)

    with engine.connect() as conn:
        result = conn.execute(
            sql.select(State.id).where(State.name == state_name))
    row = result.fetchone()
    try:
        print(f"{row[0]}")
    except TypeError:
        print("Not found")


if __name__ == "__main__":
    main()
