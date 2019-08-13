import sqlite3

connection=sqlite3.connect('example.db')
cursor=connection.cursor()

create_table="create table if not exists users(id integer primary key,username text,password text)"
create_table2="create table if not exists items(id integer primary key,name text,price real)"
create_table3="create table if not exists stores(id integer primary key,name text)"
cursor.execute(create_table2)
cursor.execute(create_table)
cursor.execute(create_table3)
connection.commit()
connection.close()
