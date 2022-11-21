import sqlite3

conn =  sqlite3.connect("customer.db")

c = conn.cursor()

# Query the database #rowid to add index
c.execute("SELECT rowid,* FROM customers")
#c.fetchone() (type:tuple)
#c.fetchmany(3)
#c.fetchall() (type:list)


# use where (operater can use : = >= <= LIKE, able to use AND OR)
# c.execute("SELECT rowid,* FROM customers WHERE last_name = 'young'")
# use LIMIT to restrict the return info
c.execute("SELECT * FROM customers WHERE email LIKE '%gmail%' LIMIT 2")
# c.execute("SELECT * FROM customers WHERE email LIKE '%gmail.com' AND last_name = 'Huang'")
print(c.fetchall())

# USE ORDER BY (if there is no parameter,it will order by ascending.
# Parameter DESC means descending)
# if it use to TEXT it will order by first letter alphabet
c.execute("SELECT rowid, *FROM customers ORDER BY first_name DESC")

items = c.fetchall()

# print their info
print("NAME ","\t\t\t EMAIL")
for item in items:
    print(item[0]," ",item[1],"\t\t",item[2])



print("\nCommand executed successfully...")

conn.commit()
conn.close()