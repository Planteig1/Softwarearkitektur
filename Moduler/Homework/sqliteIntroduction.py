import sqlite3
# Connect to a (new) database
conn = sqlite3.connect("D:\\demo\\aplha.db")

#ADD DATA
#Create a cursor
cur = conn.cursor()

#Create a "people" table
cur.execute('''CREATE TABLE IF NOT EXISTS people
            (first_name TEXT, last_name TEXT)''')
#Commit it do the db
conn.commit


# Close connection ( Correct) - DB OBJECTS
cur.close()
conn.close()