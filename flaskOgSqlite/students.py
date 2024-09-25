import sqlite3
from data_dict import random_users
import requests


def createTable():
    with sqlite3.connect('students.db') as conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS students
            (id INTEGER PRIMARY KEY , 
            first_name TEXT, 
            last_name TEXT,
            birth_date TEXT,
            email TEXT,
            phonenumber TEXT,
            address TEXT,
            nationality TEXT,
            active BOOLEAN,
            github_username TEXT
            )""")
       
    

    conn.executemany('''INSERT INTO students (
             first_name,
             last_name,
             birth_date,
             email,
             phonenumber,
             address,
             nationality,
             active,
             github_username
             ) VALUES (:first_name, :last_name, :birth_date, :email, :phonenumber, :address, :nationality, :active, :github_username)''', random_users)
    
    conn.commit()



def read():
    students = []
    with sqlite3.connect('students.db') as conn:
        cur = conn.cursor()
        allStudents = cur.execute('SELECT * FROM students')

        for row in allStudents:

            #Get the repositories
            listOfRepos = []
            headers = {
                "Authorization": "APIKEY!!!"
            }
            response = requests.get(f"https://api.github.com/users/{row[9]}/repos", headers=headers)

            repos = response.json()
            for repo in repos:
                
                if isinstance(repo, dict):
                    repoName = repo["name"]
                    listOfRepos.append(repoName)



            #Create the json format
            student = {
                'id': row[0],
                'first_name': row[1],
                'last_name': row[2],
                'birth_date': row[3],
                'email': row[4],
                'phonenumber': row[5],
                'address': row[6],
                'nationality': row[7],
                'active': row[8],
                'github_username': row[9],
                'listOfRepos': listOfRepos
            }
            students.append(student)
    
    return students

def updateUser(github_username, id):
    with sqlite3.connect('students.db') as conn:
        cur = conn.cursor()
        cur.execute("UPDATE students SET github_username = ? WHERE id = ?",(github_username, id))
        conn.commit()

def createUser(userJson):
    with sqlite3.connect('students.db') as conn:
        cur = conn.cursor()
        cur.execute('''INSERT INTO students (
             first_name,
             last_name,
             birth_date,
             email,
             phonenumber,
             address,
             nationality,
             active,
             github_username
             )VALUES (:first_name, :last_name, :birth_date, :email, :phonenumber, :address, :nationality, :active, :github_username)''', userJson)
        
        conn.commit()

def deleteUser(id):
     with sqlite3.connect('students.db') as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE id = ?",(id,))
        conn.commit()


# MAKE COMMENT AFTER INITILIZASTION - IT RUNS THE ENTIRE CODE WHEN YOU LOAD/ IMPORT IT
#createTable()
