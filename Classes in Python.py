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
#Python program to create a Vehicle class with max_speed and mileage instance attributes.
class Vehicle:
    max_speed=None
    mileage=None
 #Method
class Job:
    def __init__(self,ID=None,Salary=None,place=None):
        self.ID=ID
        self.Salary=Salary
        #By default, all the python attributes are public but can be made private specifically and can't be accessed outside the class
        self.__place=place #Private attribute
'''For accessing place
Yash(17877,320000,India)
print(Yash._Job__place)'''
    def inhand():
        return (self.Salary*0.81)
    #Class Method
    @classmethod
    def myID(cls):
        return cls.ID #Accessible without creating an object
    @staticmethod
    def paycommission():
        if Salary>120,000 and Salary<320,000:
            return "7th"
        elif Salary<=120,000:
            return "6th"
        else:
            return "8th"    
#Encapsulation
class PwdManager:
    def __init__(self,ID,Pwd):
        self.__ID=ID
        self.__Pwd=Pwd
    def login(self,ID,Pwd):
        if (self.__ID==ID) and (self.__Pwd==Pwd):
            print("Access Granted")
        else:
            print("Access Denied")
#However, using _PwdManager__ID/Pwd method on object, credentials can be known
#Inheritance
#Parent Class
class Job:
    Qt="Budh"
    def __init__(self,ID=None,Salary=None,place=None):
        self.ID=ID
        self.Salary=Salary
        #By default, all the python attributes are public but can be made private specifically and can't be accessed outside the class
        self.__place=place #Private attribute
    def inhand():
        return (self.Salary*0.81)
    #Class Method
    @classmethod
    def myID(cls):
        return cls.Qt #Accessible without creating an object
    @staticmethod
    def paycommission(Salary):
        if Salary>120000 and Salary<320000:
            return "7th"
        elif Salary<=120000:
            return "6th"
        else:
            return "8th"    
#Child class
class Employee(Job):
    def __init__(self,ID,Salary,Name):
        #Using the super() function
        super().__init__(ID,Salary)
        #Job.__init__(self,ID,Salary)
        self.Name=Name
    def printname(self):
        print(self.name)
    def nameandID(self):
        print("Name is",self.Name)
        print("ID is",self.ID)
#Polymorphism
class functions:
    def __init__(self,domain,Range,Type):
        self.domain=domain
        self.Range=Range
        self.Type=Type
    def finddomain(self):
        return self.domain
class Constant(functions):
    def __init__(self,Range,number):
        super().__init__(Range)
        self.number=number
    def finddomain(self):
        return "All Real Numbers"
#Abstract Base Class Implementation
from abc import ABC,abstractmethod

class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length


#shape = Shape()
# this code will not compile since Shape has abstract methods without
# method definitions in it
#square = Square(4)
# this will code will not compile since abstarct methods have not been
# defined in the child class, Square    
        
