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
    Base.metadata.create_all(engine)
    id = State.id
    state_name = State.name

    with engine.connect() as conn:
        result = conn.execute(
            sql.select(State).where((state_name).
                                    like("%a%")).order_by(State.id)
        )

    for row in result:
        print(f"{row.id}: {row.name}")


if __name__ == "__main__":
    main()
