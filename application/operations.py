from db import user_insert, browse_user
def register():
	username=input("Enter user namer:")
	password=input("Enter password:")
	user_insert(username,password)
	print("user created successfully!!")
def login():
	username=input("Enter user namer:")
	password=input("Enter password:")
	data = browse_user(username,password)
	if data:
		print("user login success")
		return True
	else:
		return False