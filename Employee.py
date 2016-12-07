class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

#create object of class
emp1 = Employee("Zara",2000)
emp2 = Employee("Munni",5000)

emp1.displayEmployee()
emp2.displayEmployee()

print ("Total Employee %d" %Employee.empCount)
#print ("employee._doc_:",Employee._doc_)
#print ("employee._name_:",Employee._name_)
#print ("employee._module_:",Employee._module_)
#print ("Employee._bases_:",Employee._bases_)
#print ("Employee._dict_:",Employee._dict_)
