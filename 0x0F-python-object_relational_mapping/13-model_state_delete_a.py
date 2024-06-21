#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""
from model_state import Base, State
import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base
import sys


def main():
    username, password, database = sys.argv[1:]
    engine = sql.create_engine(
        "mysql://{}:{}@localhost:\
        3306/{}".format(
            username, password, database
        )
    )

    with engine.connect() as conn:
        result = conn.execute(
            sql.delete(State)
            .values(State.name.like('%a%')))
        conn.commit()


if __name__ == "__main__":
    main()
