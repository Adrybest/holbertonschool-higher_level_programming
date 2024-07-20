#!/usr/bin/python3
"""
Lists all states starting with N from the database hbtn_0e_0_usa:

Arguments:
- mysql username
- mysql password
- database name
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
    cur.execute("SELECT * FROM states \
        WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    states = cur.fetchall()

    for row in states:
        print(row)

    cur.close()
    db.close()