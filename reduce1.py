def fun(x,y):
	return x*y
print reduce(fun,[1,2,3,4,5,6,7])
# the above reduce function will do the below job
res=fun(1,2)
for i in [3,4,5,6,7]:
	res=fun(res,i)
print(res)