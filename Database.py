import sqlite3 
db=sqlite3.connect('users.db')
cursor=db.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
               id TEXT,
               name TEXT,
               phone TEXT,
               address TEXT)
''')
async def add_to_db(name,id,phone,address):
    cursor.execute('''
INSERT INTO users(id,name,phone,address)
                   VAlUES(?,?,?,?)
                   
''',(id,name,phone,address))
    db.commit()
async def show_users():
    cursor.execute('''
SELECT id FROM users
                   ''')
    a=cursor.fetchall()
    return a