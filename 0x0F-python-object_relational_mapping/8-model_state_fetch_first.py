#!/usr/bin/python3
""" Print the first State object from database"""

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

    # Query to get the first state
    state = session.query(State).first()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    session.close()
