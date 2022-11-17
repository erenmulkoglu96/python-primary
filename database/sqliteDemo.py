import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.execute("""select FirstName, LastName from customers
where city = 'Berlin' or city = 'Prague' order by FirstName desc""")


for row in cursor:
    print("First Name = "+row[0])
    print("Last Name = "+row[1])
    print("*****")

connection.close()
# %%
import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.execute("""select city, count(*) from customers
group by city having count(*)>1 order by count(*) desc""")

for row in cursor:
    print("City = "+row[0])
    print("Count = "+str(row[1]))
    print("*****")

connection.close()
#%%
import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.execute("""select FirstName, LastName, City from customers
where city like '%s' order by FirstName""")

for row in cursor:
    print("FirstName = " + row[0])
    print("LastName = " + row[1])
    print("City = " + row[2])
    print("\n")

connection.close()