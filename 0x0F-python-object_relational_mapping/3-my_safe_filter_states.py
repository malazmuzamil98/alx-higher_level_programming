#!/usr/bin/python3
"""list states"""
import MySQLdb
import sys


def main():
    if len(sys.argv) != 5:
        print("Usage: {} username password \
            database state_name".format(sys.argv[0]))
        sys.exit(1)
    username, password, database, state = sys.argv[1:]
    conn = MySQLdb.connect(
        host="localhost", user=username, password=password, db=database
    )
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cur.execute(query, (state,))
    items = cur.fetchall()
    for item in items:
        print(item)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
