def fun(a,b):
	try:
		return a+b
	except:
		return None
def check_even(x=0):
	try:
		if x%2==0:
			return "EVEN"
		else:
			return "ODD"
	except:
		return None

