# Data hiding example 

class JustCounter:
 __secretCount = 0

 def count(self):
  self.__secretCount += 1
  print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print (counter._JustCounter.__secretCount)
print (counter.__secretCount)
