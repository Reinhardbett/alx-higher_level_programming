#!/usr/bin/python3
""" Print State object with name passed as arg"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db}'
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to get the specific state id
    states = session.query(State)\
        .filter(State.name == state_name)\
        .all()

    # Print state id of specific state from list
    if states:
        print(f"{states[0].id}")
    else:
        print("Not found")

    session.close()
