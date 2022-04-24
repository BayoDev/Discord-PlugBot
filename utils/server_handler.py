import sqlite3 as sql
import os

lastPath: str
workPath: str

def query(inside) -> list:
    global workPath
    global lastPath

    lastPath = os.getcwd()

    os.chdir(workPath)

    con = sql.connect('../data/database.db')
    cur = con.cursor()
    response = cur.execute(inside).fetchall()
    con.commit()
    con.close()

    os.chdir(lastPath)

    return response


def table_exists(table_name) -> bool:
    global workPath
    global lastPath
    lastPath = os.getcwd()

    os.chdir(workPath)

    con = sql.connect('../data/database.db')
    cur = con.cursor()
    if len(cur.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'").fetchall()) == 0:
        return False
    con.commit()
    con.close()

    os.chdir(lastPath)

    return True


def setup():
    global workPath
    workPath = os.getcwd()
    if not os.path.isfile('../data/database.db'):
        with open('../data/database.db', 'w')as file:
            pass
    return