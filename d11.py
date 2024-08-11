# inheritance 
# class Employee:
#     company = "ITC"
#     def show(self):
#         print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")


# class Programmer(Employee):
#     company = "ITC Infotech"
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")


# a = Employee()
# b = Programmer()

# print(a.company, b.company)

# multiple inheritances 
# class Employee:
#     company = "ITC"
#     name = "Default name"
#     def show(self):
#         print(f"The name of the Employee is {self.name} and the company is {self.company}")

# class Coder:
#     language = "Python"
#     def printLanguages(self):
#         print(f"Out of all the languages here is your language: {self.language}")
     


# class Programmer(Employee, Coder):
#     company = "ITC Infotech"
#     def showLanguage(self):
#         print(f"The name is {self.company} and he is good with {self.language} language")


# a = Employee()
# b = Programmer()

# b.show()
# b.printLanguages()
# b.showLanguage()

# multilevel inheritances 
# class Employee:
#     a = 1 

# class Programmer(Employee):
#     b = 2 

# class Manager(Programmer):
#     c = 3

# o = Employee()
# print(o.a) # Prints the a attribute
# # print(o.b) # Shows an error as there is no b attribute in Employee class

# o = Programmer()
# print(o.a, o.b)


# o = Manager()
# print(o.a, o.b, o.c)

# super keyword 
# class Employee:
#     def __init__(self):
#         print("Constructor of Employee")
#     a = 1 

# class Programmer(Employee):
#     def __init__(self):
#         print("Constructor of Programmer")
#     b = 2 

# class Manager(Programmer):
#     def __init__(self):
#         super().__init__()
#         print("Constructor of Manager")
#     c = 3

# o = Employee()
# print(o.a) # Prints the a attribute 

# o = Programmer()
# print(o.a, o.b)


# o = Manager()
# print(o.a, o.b, o.c)

# class methods
# class Employee:
#     a = 1
    
#     @classmethod
#     def show(cls):
#         print(f"The class attribute of a is {cls.a}")

# e = Employee()
# e.a = 45

# e.show()

# property decorator 
# class Employee:
#     a = 1
    
#     @classmethod
#     def show(cls):
#         print(f"The class attribute of a is {cls.a}")

#     @property 
#     def name(self):
#         return f"{self.fname} {self.lname}"
    
#     @name.setter
#     def name (self,value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]

# e = Employee()
# e.a = 45

# e.name = "Harry Khan"
# print(e.fname, e.lname)

# e.show()

# operator overloading 
# class Number:
#     def __init__(self, n):
#         self.n = n

#     def __add__(self, num):
#         return self.n + num.n

# n = Number(1)
# m = Number(2)

# print(n + m)

# practise set -11 
# 1
# class TwoDVector:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j
    
#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j ")
        

# class ThreeDVector(TwoDVector):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.k = k

#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

# a = TwoDVector(1, 2)
# a.show()
# b = ThreeDVector(5, 2, 3)
# b.show()

# 2
# class Animals:
#     pass 

# class Pets(Animals):
#     pass 

# class Dog(Pets):

#     @staticmethod
#     def bark():
#         print("Bow Bow!")


# d = Dog()

# d.bark()

# 3
# class Employee:
#     salary = 234
#     increment = 20 
    
#     @property
#     def salaryAfterIncrement(self):
#         return (self.salary + self.salary * (self.increment/100))

#     @salaryAfterIncrement.setter 
#     def salaryAfterIncrement(self, salary):
#         self.increment =  ((salary/self.salary) -1)*100 




# e = Employee()
# print(e.salaryAfterIncrement)
# e.salaryAfterIncrement = 280.8
# print(e.increment)

# 4
# class Complex:
#     def __init__(self, r, i):
#         self.r = r
#         self.i = i

#     def __add__(self, c2):
#         return Complex(self.r + c2.r, self.i + c2.i)
    
#     def __mul__(self, c2):
#         real_part = self.r * c2.r - self.i * c2.i
#         imag_part = self.r * c2.i + self.i * c2.r
#         return Complex(real_part, imag_part)
    
#     def __str__(self):
#         return f"{self.r} + {self.i}i"
        
    

# c1 = Complex(1, 2)
# c2 = Complex(3, 4)
# print(c1 + c2)
# print(c1*c2)

# 5
# class Vector:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __add__(self, other):
#         result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
#         return result

#     def __mul__(self, other):
#         result = self.x * other.x + self.y * other.y + self.z * other.z
#         return result

#     def __str__(self):
#         return f"Vector({self.x}, {self.y}, {self.z})"

# Test the implementation
# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)
# v3 = Vector(7, 8, 9)  # Same dimension vector

# print(v1 + v2)  # Output: Vector(5, 7, 9)
# print(v1 * v2)  # Output: 32

# print(v1 + v3)  # Output: Vector(8, 10, 12)
# print(v1 * v3)  # Output: 50

# 6
# class Vector:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __add__(self, other):
#         result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
#         return result

#     def __mul__(self, other):
#         result = self.x * other.x + self.y * other.y + self.z * other.z
#         return result

#     def __str__(self):
#         return f"{self.x}i + {self.y}j + {self.z}k"

# # Test the implementation
# v1 = Vector(1, 2, 3)
# v2 = Vector(4, 5, 6)
# v3 = Vector(7, 8, 9)  # Same dimension vector

# print(v1 + v2)  # Output: Vector(5, 7, 9)
# print(v1 * v2)  # Output: 32

# print(v1 + v3)  # Output: Vector(8, 10, 12)
# print(v1 * v3)  # Output: 50

# 7
# class Vector:
#     def __init__(self, l): 
#         self.l = l

    
    
#     def __len__(self):
#         return len(self.l)

# # Test the implementation
# v1 = Vector([1, 2, 3]) 
# print(len(v1))