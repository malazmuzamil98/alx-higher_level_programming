#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""
from model_state import Base, State
from model_city import City
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
        query = sql.select(State.name, City.id, City.name).\
            join(City, State.id == City.state_id).order_by(City.id)
        result = conn.execute(query)
        result = result.fetchall()
        for row in result:
            print("{}: ({}) {}".format(row[0], row[1], row[2]))


if __name__ == "__main__":
    main()
