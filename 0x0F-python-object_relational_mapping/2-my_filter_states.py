#!/usr/bin/python3
'''This script lists all states in the hbtn_0e_0_usa starting with uppercase N
It then takes in an arg and displays all values that match it
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

    # Display table states in ascending order by states.id
    # Specify the state name from the SQL query
    query = """SELECT * FROM states\
        WHERE name LIKE BINARY '{}'\
        ORDER BY id ASC""".format(sys.argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close connection to database and working environment
    cur.close()
    db.close()
