from operations import register,login
while True:
	print("HOME SCREEN\n\t1.LOGING\n\t2.REGISTER\n\tq.quit")
	opt=input("enter an option:")
	if opt.lower()=="q":
		print("Thank you!!")
		break
	if opt=="2":
		register()
	elif opt=="1":
		flag=login()
		if flag:
			print("Customer menu:\n\t1.create\n\t2.update\n\t3.delete\n\t4.\
				reports")
			cust_opt=input("Enter an option:")
	else:
		print("wrong option")
