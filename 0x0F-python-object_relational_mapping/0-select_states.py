#!/usr/bin/python3
'''This script lists all elements from table states present
in the database hbtn_0e_0_usa
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
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close connection to database and working environment
    cur.close()
    db.close()
