import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

# insert a customer
c.execute("INSERT INTO customers VALUES ('Peter','young','peteryang10@gmail.com')")

# insert mutiple customer
many_customers = [
                    ('Hank','Huang','hank@gmail.com'),
                    ('JP','Pan','JP@gmail.com')
]
# should use insert many
c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)


print("Command executed successfully... ")
# commit our command
conn.commit()
# clsoe our connection
conn.close()

