fun=lambda x:"EVEN" if x%2==0 else "ODD"
l=range(650000000)
print(map(fun,l))