# raising and exception 
def fun(level):
 if level < 1 :
  raise Exception(level)

 return level

try :
# l = fun(5)
 l = fun(-5)
 print ("level : ",l)
except Exception as e:
 print ("Error in level argument",e.args[0])
else :
 print ("no exception caught")
finally :
 print ("In finally block")
