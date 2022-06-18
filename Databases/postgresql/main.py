
import time
from venv import create
import psycopg2
from pprint import pprint
import json

from setuptools import Command
# create a table using python.
"""
with psycopg2.connect(user = "postgres", password = "class2020",host = "postgres.cb9lsm3vngxa.us-east-1.rds.amazonaws.com",port = "5432", database = "postgres") as connection:
    cursor = connection.cursor()
    print("Print postgres server infomation")
    print(connection.get_dsn_parameters(), "\n")
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

"""
"""
with psycopg2.connect(user = "postgres", password = "class2020",host = "postgres.cb9lsm3vngxa.us-east-1.rds.amazonaws.com",port = "5432", database = "postgres") as connection:
    cursor = connection.cursor()
    create_table = connection.cursor()
    print("creating tables in my database")
    time.sleep(4)
    create_table = ''' CREATE TABLE Kojitechs
        (ID INT PRIMARY KEY  NOT NULL,
        FIRST_NAME TEXT NOT NULL,
        LASY_NAME  TEXT NOT NULL,
        PRICE   REAL);'''

    cursor.execute(create_table) 
    connection.commit()
    print("Table create sucessfully in PostgreSQL")  


"""
"""
'''CREATE TABLE students
        (ID INT PRIMARY KEY    NOT NULL,
        STUT_NAME  TEXT NOT NULL ,
        Email   TEXT NOT NULL,
        Phone_Number   TEXT NOT NULL,
        STUT_ADD TEXT NOT NULL,
        STUT_APP TEXT NOT NULL,
        zip INT NOT NULL,
        Amount_paid REAL NOT NULL,
        PaidFull bool NOT NULL);
    '''

"""
"""
# insert in a  table
students = json.loads(Path("studentinfo.json").read_text())
#print(students)

with psycopg2.connect(user = "postgres", password = "class2020",host = "postgres.cb9lsm3vngxa.us-east-1.rds.amazonaws.com",port = "5432", database = "postgres") as connection:
    cursor = connection.cursor()
    #create_table = connection.cursor()
    print("inserting data to postgres database")
    time.sleep(4)

    command = "INSERT INTO students VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    for student in students:
        cursor.execute(command, tuple(student.values()))
    connection.commit()
    print(" Table Inserted sucessfully in PostgreSQL")  
"""
# Reading a table
"""
with psycopg2.connect(user = "postgres", password = "class2020",host = "postgres.cb9lsm3vngxa.us-east-1.rds.amazonaws.com",port = "5432", database = "postgres") as connection:
    cursor = connection.cursor()
    time.sleep(4)
    command = "SELECT * FROM students"
    cursor.execute(command)
    datas = cursor.fetchall()
    for data in datas:
        print(data)
"""
