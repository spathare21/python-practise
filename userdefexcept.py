# User defined exception 
class Networkerror(RuntimeError) :
 def _init_(self,arg):
  self.args = arg

try :
 raise Networkerror("Bad hostname")
except Networkerror as e:
 print (e.args)
