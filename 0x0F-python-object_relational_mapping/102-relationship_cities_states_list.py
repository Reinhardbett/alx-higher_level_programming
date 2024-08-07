#!/usr/bin/python3
"""Script to fetch city by state"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


def list_all_city_object():
    """This function lists all city objects
    from the database hbtn_0e_101_usa.
    """

    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db}'
        )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State)\
                              .join(State, State.id == City.state_id)\
                              .order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, state.name))


if __name__ == "__main__":
    list_all_city_object()
