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
    try:
        cursor.execute("""CREATE TABLE userData
                    (uId text, 
                    uClass text)""")
        cursor.commit()
    except BaseException:      
        print("base hasn't created")

intilisation()


def reg(uId, uClass):
    cursor.execute("SELECT * FROM userData")
    l1 = cursor.fetchall()
    cursor.execute(reregRequest, (uClass,uId))
    conn.commit()
    cursor.execute("SELECT * FROM userData")
    l2 = cursor.fetchall()
    if l1 == l2:
        cursor.execute(regRequest, (uId, uClass))
        conn.commit()
    cursor.execute("SELECT uId, MIN(ROWID) FROM userData")
    l3 = cursor.fetchall()
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
        h1 = h0[0][0]
        return h1
    except BaseException:
        return 0

def getUserId(uClass):
    cursor.execute(getUIdRequest, [(uClass)])
    q0 = cursor.fetchall()
    q1 = []
    for i in range (len(q0)):
        q1.append(q0[i][0])
    return q1

def getStat():
    cursor.execute("SELECT * FROM userData")
    print (cursor.fetchall())