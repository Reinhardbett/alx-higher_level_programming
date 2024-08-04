#!/usr/bin/python3
'''This script lists all cities from database hbtn_0e_4_usa
'''
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database
    # Take username, password, and database name from stdout
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create working environment for our connection
    cur = db.cursor()

    # List cities with their corresponding state names
    # Order results by cities.id
    query = "SELECT cities.id, cities.name, states.name\
        FROM cities\
        INNER JOIN states ON cities.state_id = states.id\
        ORDER BY cities.id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close connection to database and working environment
    cur.close()
    db.close()
