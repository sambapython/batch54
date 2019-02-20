class Emp:
    a=10
    b=20
    def op1(c,d):
    	print(ref,id(ref))
        print("this is op1:",c,d)
print(Emp.a,Emp.b)
ref=Emp()
print(ref,id(ref))
r1=Emp.op1(ref,2000)
