import sqlite3
conn=sqlite3.connect('db1')
curr=conn.cursor()
tbcmd='create table rajat(name varchar(200))'