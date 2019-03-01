print("welcome")
a=10
b=20
c=a+b
def fun(x,y):
	import pdb;pdb.set_trace()
	print(x,y)
	try:
		z=x-y
		return z
	except:
		return None
d=2000
for i in range(-2,4):
	if i!=0:
		print(10/i)
fun(100,50)
print("thank you")
