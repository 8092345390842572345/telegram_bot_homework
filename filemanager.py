import sqlite3

conn = sqlite3.connect('dateBase.sqlite')
cursor = conn.cursor()

# it works. As a useless code

reregRequest = """
    UPDATE userData 
    SET uClass = '?' 
    WHERE uId = '?'
"""

regRequest = """
    INSERT INTO userData VALUES (?,?)
"""



def intilisation():
    try:
        cursor.execute("""CREATE TABLE userData
                    (uId text, 
                    uClass text)""")
    except BaseException:  # couse I don't know how to fix it
        print("base hasn't created. It can already exist or this code sucks")


# help me please

def reg(uId, uClass):
    try:
        print("1")
        cursor.execute(reregRequest, (uClass, uId))
        conn.commit()
        print("rereg")
    except BaseException:
        print("2")
        cursor.execute(regRequest, (uClass, uId))
        print("reg")
    conn.commit()

# fuck this code

intilisation()
reg("12", "2")