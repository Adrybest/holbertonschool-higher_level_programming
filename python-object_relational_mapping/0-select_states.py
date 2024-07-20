#!/usr/bin/python3
"""
lists all states from the database `hbtn_0e_0_usa`.

Arguments:
    username: username of the MySQL
    password: password of the MySQL
    database: database name of the MySQL server
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()

    for row in states:
        print(row)

    cur.close()
    db.close()