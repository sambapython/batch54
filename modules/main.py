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
'''
import sys
print(sys.path)
import file1
file1.fun()
print(file1.a,file1.b,file1.c)
'''
'''
import sys
#sys.path.append("/home/khyaathipython/")
sys.path.insert(1,"/home/khyaathipython/")
print(sys.path)
import file2
'''
#import folder1
#import folder1
#folder1.f1.fun()
'''
from folder1 import f1,f2
f1.fun()
f2.fun()
'''
from folder1 import f1
f1.fun()
