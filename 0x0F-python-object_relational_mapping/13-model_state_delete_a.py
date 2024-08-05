#!/usr/bin/python3
""" Delete all State objects with letter a"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db}'
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to get the specific states
    states_with_a = session.query(State)\
        .filter(State.name.like('%a%'))\
        .all()

    # Loop through the states and delete
    for state in states_with_a:
        session.delete(state)
    session.commit()

    session.close()
