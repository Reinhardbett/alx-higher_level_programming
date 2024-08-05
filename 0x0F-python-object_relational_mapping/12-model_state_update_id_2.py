#!/usr/bin/python3
""" Change name of a State object"""

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

    # Retrieve and update specific State object
    state_to_update = session.query(State)\
        .filter(State.id == 2)\
        .first()
    if state_to_update:
        state_to_update.name = "New Mexico"
    session.commit()

    session.close()
