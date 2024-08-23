# 0x0F. Python - Object-relational mapping

## Background
Pre-configured databases will be linked to using MySQLdb and SQLAlchemy
### Without ORM
```python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
### With ORM
```python
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

## General Requirements
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files will be executed with MySQLdb version 2.0.x
- All files will be executed with SQLAlchemy version 1.4.x
- First line of all files should be exactly #!/usr/bin/python3
- All code should be pycodestyle-compliant (version 2.8.*)

### Install MySQLdb module verstion 2.0.x
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info
(2, 0, 3, 'final', 0)
```

### Install SQLAlchemy module version 1.4.x
```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.4.22'
```

## SQLAlchemy Object Relational Mapper Tutorial
SQLAlchemy ORM helps map python classes to database tables.
When using ORM we must first describe the database tables then define classes we will map to these tables
- Connect by first calling an engine using `create_engine`, here we have not yet connected to the database.
```
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
```
- Classes we define will use elements of a base class provided 
```
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
```
- We can now define classes from this base that will shape how we want our tables to look.
- The class must define details about the table which we will be mapping.
- At minimum it must have the tablename attribute and one column which is a primary key
```
from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)
```

