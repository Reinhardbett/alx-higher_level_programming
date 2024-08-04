#!/usr/bin/python3
'''This script takes a state name as an argument
It then lists all its cities using hbtn_0e_4_usa
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

    # Specifically return only those cities from given state
    # Avoid SQL injection risks
    # Order results by cities.id
    query = "SELECT cities.name\
        FROM cities\
        INNER JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s\
        ORDER BY cities.id ASC"
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()

    # Create a list of tuples and output as string
    print(", ".join([row[0] for row in rows]))

    # Close connection to database and working environment
    cur.close()
    db.close()
