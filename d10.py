# class Employee: 
#     language = "Py" # This is a class attribute
#     salary = 1200000


# harry = Employee()
# harry.name = "Harry" # This is an instance attribute
# print(harry.name, harry.language, harry.salary)

# rohan = Employee()
# rohan.name = "Rohan Roro Robinson"
# print(rohan.name, rohan.salary, rohan.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class

# instances vs class attre 
# class Employee: 
#     language = "Python" # This is a class attribute
#     salary = 1200000


# harry = Employee()
# harry.language = "JavaScript" # This is an instance attribute
# print(harry.language, harry.salary)

# self keword 
# class Employee: 
#     language = "Python" # This is a class attribute
#     salary = 1200000

#     def getInfo(self):
#         print(f"The language is {self.language}. The salary is {self.salary}")

#     @staticmethod
#     def greet():
#         print("Good morning")


# harry = Employee()
# harry.language = "JavaScript" # This is an instance attribute
# harry.greet()
# harry.getInfo() 
# Employee.getInfo(harry)

# constructor 
# class Employee: 
#     language = "Python" # This is a class attribute
#     salary = 1200000

#     def __init__(self, name, salary, language): # dunder method which is automatically called
#         self.name = name
#         self.salary = salary
#         self.language = language
#         print("I am creating an object")
 
 
#     def getInfo(self):
#         print(f"The language is {self.language}. The salary is {self.salary}")

#     @staticmethod
#     def greet():
#         print("Good morning")


# harry = Employee("Harry", 1300000, "JavaScript") 
# # harry.name = "Harry"
# print(harry.name, harry.salary, harry.language)

# rohan = Employee()

# practise set-10 
# 1
# class Programmer:
#     company = "Microsoft"
#     def __init__(self, name, salary, pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin


# p = Programmer("Harry", 1200000, 245001)
# print(p.name, p.salary, p.pin, p.company)
# r = Programmer("Rohan", 1200000, 245001)
# print(r.name, r.salary, r.pin, r.company)

# 2
# class Calculator:
#     def __init__(self, n):
#         self.n = n 
    
#     def square(self):
#         print(f"The square is {self.n*self.n}")

#     def cube(self):
#         print(f"The cube is {self.n*self.n*self.n}")

#     def squareroot(self):
#         print(f"The squareroot is {self.n**1/2}")

# a = Calculator(4)
# a.square()
# a.cube()
# a.squareroot()

# 3
# class Demo:
#     a = 4

# o = Demo()
# print(o.a) # Prints the class attribute because instance attribute is not present
# o.a = 0 # Instance attribute is set
# print(o.a) # Prints the instance attribute because instance attribute is present
# print(Demo.a) # Prints the class attribute

# 4
# class Calculator:
#     def __init__(self, n):
#         self.n = n 
    
#     def square(self):
#         print(f"The square is {self.n*self.n}")

#     def cube(self):
#         print(f"The cube is {self.n*self.n*self.n}")

#     def squareroot(self):
#         print(f"The squareroot is {self.n**1/2}")
    
#     @staticmethod
#     def hello():
#         print("Hello there!")

# a = Calculator(4)
# a.hello()
# a.square()
# a.cube()
# a.squareroot()

# 5
# from random import randint

# class Train:

#     def __init__(self, trainNo):
#         self.trainNo = trainNo

#     def book(self, fro, to):
#         print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}") 

#     def getStatus(self):
#         print(f"Train no: {self.trainNo} is running on time") 

#     def getFare(self, fro, to):
#         print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")  


# t = Train(12399)
# t.book("Rampur", "Delhi")
# t.getStatus()
# t.getFare("Rampur", "Delhi")

# 6
# from random import randint

# class Train:

#     def __init__(slf, trainNo):
#         slf.trainNo = trainNo

#     def book(harry, fro, to):
#         print(f"Ticket is booked in train no: {harry.trainNo} from {fro} to {to}") 

#     def getStatus(self):
#         print(f"Train no: {self.trainNo} is running on time") 

#     def getFare(self, fro, to):
#         print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")  


# t = Train(12399)
# t.book("Rampur", "Delhi")
# t.getStatus()
# t.getFare("Rampur", "Delhi")

