#!/usr/bin/python3
""" Add State object Louisiana to database"""

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

    # Query processes to add new State object
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print state id of newly-added state
    print(f"{new_state.id}")

    session.close()
