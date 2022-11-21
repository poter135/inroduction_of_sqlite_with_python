import sqlite3

conn = sqlite3.connect("customer.db")
c = conn.cursor()

# use row id to update is better
c.execute("""UPDATE customers SET first_name = 'Bob'
            WHERE rowid = '2'
""")

# DELETE
c.execute("DELETE FROM customers WHERE rowid = 5")
conn.commit()

# DROP TABLE
#   c.execute("DROP TABLE customers")
conn.commit()


items = c.fetchall()

for item in items:
    print(item)




print("\nCommand executed successfully...")

conn.commit()
conn.close()