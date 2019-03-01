import logging
logging.basicConfig(level=logging.DEBUG,
    filename="log.txt",
    format="%(asctime)s==>%(levelname)s=>%(message)s")
print("welcome")
logging.info("welcome")
a=input("enter a value:")
logging.info("a value given by user")
b=input("Enter b value:")
logging.info("user entered b value")
f=open("res.csv","a")
logging.info("open a file in append mode")
s="\nbefore conversion a=%s,b=%s"%(a,b)
#print(s)
logging.debug("before conversion a=%s,b=%s"%(a,b))
f.write(s)
try:
    a=float(a)
    logging.info("a value converted")
    b=float(b)
    logging.info("b value converted")
    s="after conversion a=%s,b=%s"%(a,b)
    #print(s)
    logging.debug(s)
    res=a/b
    logging.info("calculated the resule")
    print("RESULT:%s"%res)
    logging.debug("Result=%s"%res)
    f.write(",res=%s"%res)
    logging.info("writing the result in to file.")
except ZeroDivisionError as err:
    logging.error("dont enter zero for b")
    print("dont enter zero for b")
except ValueError as err:
    logging.error("expecting only digits for a and b")
    print("expecting only digits for a and b")
except Exception as err:
    logging.error("%s"%err)
    print(err)
    #print("something went wrong")
f.close()
logging.info("Thank you!!")
print("Thank you!!")
print("some statements in main")