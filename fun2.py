#default function parameter example
def printinfo(name,age=22):
 print ("Name :", name)
 print ("Age :",age)

printinfo(age=50,name="mike")
printinfo(name="harvey")

print ("\n\n")

#variable lenght arguments
def printdata(arg1,*vartuple): 
 print ("Output is :")
 print (arg1)
 for var in vartuple:
  print (var)

printdata(10)
printdata(70,23,40)

print ("\nanonymous functions \n")

sum = lambda arg1,arg2:arg1+arg2

print ("value of total:", sum(10,20))
print ("total is :",sum(21,21))
