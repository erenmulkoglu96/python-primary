import sqlite3

def updateCustomer():

    connection = sqlite3.connect("chinook.db")

    connection.execute("""update customers set city = 'İstanbul' where city = 'Ankara'""")

    connection.commit()
    connection.close()

updateCustomer()