import sqlite3

conn = sqlite3.connect('dateBase.db')
cursor = conn.cursor()
# conn.row_factory = sqlite3.Row

# it works. As a useless code

reregRequest = """
    UPDATE userData 
    SET uClass = ? 
    WHERE uId = ?
"""

regRequest = """
    INSERT INTO userData VALUES (?,?)
"""



def intilisation():
    try:
        cursor.execute("""CREATE TABLE userData
                    (uId text, 
                    uClass text)""")
        cursor.commit()
    except BaseException:  # couse I don't know how to fix it
        print("base hasn't created. It can already exist or this code sucks")


# help me please

def reg(uId, uClass):
    cursor.execute("SELECT * FROM userData")
    l1 = cursor.fetchall()
    print("1")
    cursor.execute(reregRequest, (uClass,uId))
    conn.commit()
    print("rereg")
    cursor.execute("SELECT * FROM userData")
    l2 = cursor.fetchall()

    if l1 == l2:
        print("2")
        cursor.execute(regRequest, (uId, uClass))
        conn.commit()
        print("reg")
    cursor.execute("SELECT uId, MIN(ROWID) FROM userData")
    l3 = cursor.fetchall()
    print(l3)
    cursor.execute("""
        DELETE FROM userData
        WHERE rowid NOT IN (
        SELECT MIN(rowid) 
        FROM userData 
        GROUP BY uId
    )""")
    conn.commit()


# fuck this code

intilisation()
reg('id4', 'class31')
cursor.execute("SELECT * FROM userData")
print (cursor.fetchall())
conn.close()

# I did it