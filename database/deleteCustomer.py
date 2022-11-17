import sqlite3

def deleteCustomer():

    connection = sqlite3.connect("chinook.db")

    connection.execute("Delete from customers where city = 'İstanbul'")

    connection.commit()
    connection.close()

deleteCustomer()