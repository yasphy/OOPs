#Most Basic declaration without any object
class ClassName:
    pass
#Declaration with an object
class MyClass:
    pass

obj = MyClass()  # creating a MyClass Object
print(obj)
#Output is the memory address of the object
# Defining Class properties
class Main:
  ID=17877
  Salary=320,000
 
 Yash=Main()
 #Accessing properties
 print(Yash.ID) #ID of Yash 
 print(Yash.Salary) #Salary of Yash
 #One can also Assign values to properties outside class as well
 class Main:
  ID=None
  Salary=None
 
 Yash=Main()
 Yash.ID=17877
 Yash.Salary=320,000
 #Declaring one more property/Attribute
 Yash.Qualification=Graduate
 #Similar accessing part
 print(Yash.ID)  
 print(Yash.Salary)
 print(Yash.Qualification)
 #Exploring the initialize property
 class Main:
  def __init__(self,ID,Salary,Qualification):
    self.ID=ID
    self.Salary=Salary
    self.Qualification=Qualification
 
 Yash=Main(17877,320,000,Graduate)
 #Again same access results
 # The initial method generates instance variable whereas directly declaring properties class generate class variables and following example explains it
 class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables
 #Any change in class variable is reflected in all object and hence,should be used carefully
 
