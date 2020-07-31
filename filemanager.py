import sqlite3

def intelisation():
    conn = sqlite3.connect('dateBase.sqlite')

    cursor = conn.cursor()

    try:
        cursor.execute("""CREATE TABLE userData
                    (id text, 
                    uClass text)""")
    except BaseException:
        pass