import json
import psycopg2
def connect():
	f=open("config.json")
	data=json.load(f)
	database=data.get("database")
	con=psycopg2.connect(host=database.get("host"),
						user=database.get("user"),
						password=database.get("password"),
						database=database.get("database"),
						port=database.get("port"))
	return con,con.cursor()
def user_insert(username,password):
	con,cur=connect()
	cur.execute("insert into users(name,password) values('%s','%s')\
		"%(username,password))
	con.commit()
	con.close()
def browse_user(username,password):
	con,cur=connect()
	cur.execute("select * from users where name='%s' and password='%s'\
		"%(username,password))
	return cur.fetchone()

if __name__ == "__main__":
	con,cur=connect()
	cur.execute("create table customers(id serial primary key, name \
		varchar(250))")
	cur.execute("create table users(id serial primary key, name \
		varchar(250), password varchar(250))")
	con.commit()
	con.close()