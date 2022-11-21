import sqlite3




def show_all():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, *FROM customers")
    items = c.fetchall()
    for item in items:
        print(item)

    conn.commit()
    conn.close()

def add_one(first,last,email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)",(first,last,email))
    conn.commit()
    c.close()

def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid = (?)",id)
    conn.commit()
    c.close()