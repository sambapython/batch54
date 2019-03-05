l=[1,2,3,4]
k=[5,6,7,8,9,10]
def fun(x,y):
	print "x=%s,y=%s"%(x,y)
	return x+y
print(map(fun,l,k))
	