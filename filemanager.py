import sqlite3




conn = sqlite3.connect('dateBase.db', check_same_thread = False)
cursor = conn.cursor()

reregRequest = """
    UPDATE userData 
    SET uClass = ? 
    WHERE uId = ?
"""

regRequest = """
    INSERT INTO userData VALUES (?,?)
"""

getUIdRequest = """
    SELECT uId
    FROM userData 
    where uClass = ?;
"""

getUClassRequest = """
    SELECT uClass
    FROM userData 
    where uId = ?;
"""


def intilisation():
# conn.row_factory = sqlite3.Row

# it works. As a useless code

    try:
        cursor.execute("""CREATE TABLE userData
                    (uId text, 
                    uClass text)""")
        cursor.commit()
    except BaseException:  # couse I don't know how to fix it
        print("base hasn't created. It can already exist or this code sucks")

intilisation()

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
    print(type(l2[0]))
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

def getUserClass(uId):
    try:
        cursor.execute(getUClassRequest, [(uId)])
        h0 = cursor.fetchall()
        print (h0)
        h1 = h0[0][0]
        print(h1)
        return h1
    except BaseException:
        return 0

def getUserId(uClass):
    cursor.execute(getUIdRequest, [(uClass)])
    print (cursor.fetchall())
    return cursor.fetchall()

def getStat():
    cursor.execute("SELECT * FROM userData")
    print (cursor.fetchall())

# fuck this code

# reg('id4', 'class31')
cursor.execute("SELECT * FROM userData")
print (cursor.fetchall())
# conn.close()

getUserClass('722810009')
# I did it
# 722810009