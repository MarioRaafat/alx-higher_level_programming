#!/usr/bin/python3
""" script that takes in the name of a state as an argument and lists all cities of that state """
import MySQLdb
import sys


if __name__ = "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute(""" SELECT cities.name FROM cities JOIN states 
            ON cities.state_id= states.id WHERE states.name = %s""", (sys.argv[4],))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
