#!/usr/bin/python3
"""Script to fetch city by state"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


def db_engine():
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db}'
        )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(City, State).\
        filter(City.state_id == State.id).all()
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()


if __name__ == "__main__":
    db_engine()
