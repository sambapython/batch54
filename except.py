import time
print("hello")
try:
    print("try")
    #print(1/0)
    time.sleep(30)
except Exception as err: 
    print(err)
except:
    print("except")
finally:
    print("finally")

print("thank yu")