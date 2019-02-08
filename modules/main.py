'''
import file1
file1.fun()
print(file1.a,file1.b,file1.c)
'''
'''
from file1 import a,b,c,fun 
print(a)
print(b)
print(c)
fun()
'''
import sys
print(sys.path)
import file1
file1.fun()
print(file1.a,file1.b,file1.c)