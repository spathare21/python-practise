#Argument of an exception additional info about the problem
def temp(var):
 try :
  return int(var)
 except ValueError as e:
  print ("The argument does not contains numeber \n",e)
 
temp("xyz")
print ("value returned",temp(123))
