import sqlite3

conn = sqlite3.connect('customer.db')

#create a cursor
c = conn.cursor()

#create a table #execute is case seneitive
c.execute("""CREATE TABLE customers(
    first_name TEXT,
    last_name TEXT,
    email TEXT
)""")
#only use one """ should type in one line

#NULL
#INTEGER
#REAL(float)
#TEXT
#BLOB(img)

#commit out commend
conn.commit()

#close our connection
conn.close()


