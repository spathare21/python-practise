#inheritance example 

class Parent:
 parentAttr = 100
 def _init_(self):
  print ("calling parent contructor")
 
 def parentMethod(self):
  print ("Calling parent mehtod")
 
 def demo(self):
  print ("parent demo")

 def setAttr(self,attr):
  Parent.parentAttr = attr

 def getAttr(self):
  print ("Parent Attribute :",Parent.parentAttr)

class Child(Parent): 
 def _init_(self):
  print("Calling child contructor")

 def demo(self):
  print ("Child demo")

 def childMethod(self):
  print ("Calling child method")

c= Child()          #Instance of child 
c.childMethod()     # Child call its method
c.parentMethod()    # calls parent's method
c.setAttr(200)      # again call parent method
c.getAttr()         # call parent method
c.demo()

c =  Parent()
c.parentMethod()

