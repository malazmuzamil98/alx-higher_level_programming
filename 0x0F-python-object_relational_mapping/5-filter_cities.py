#!/usr/bin/python3
"""list citys"""
import MySQLdb
import sys


def main():
    username, password, database, state = sys.argv[1:]
    conn = MySQLdb.connect(
        host="localhost", user=username, password=password, db=database
    )
    cur = conn.cursor()
    query = "SELECT cities.name \
        FROM cities \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s \
        ORDER BY cities.id ASC"
    cur.execute(query, (state,))
    cities = [row[0] for row in cur.fetchall()]

    # Print the results as comma-separated string
    print(', '.join(cities))
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
