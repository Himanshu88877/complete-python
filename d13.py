# lambda function 
# def square(n):
#     return n*n 
# square = lambda x: x*x
# print(square(5))

# join function 
# a = ["Harry", "Rohan", "Shubham"]
# final = "::".join(a)
# print(final)

# format function 
# a = "{1} is a good {0}".format("harry", "boy")

# print(a)

# map filter and reduced 
# from functools import reduce
# Map Example 
# l = [1, 2, 3, 4, 5]

# square = lambda x: x*x

# sqList = map(square, l)
# print(list(sqList))

# Filter Example
# def even(n):
#     if (n%2 == 0):
#         return True 
#     return False

# onlyEven= filter(even, l)
# print(list(onlyEven))

# Reduce Example
# def sum(a, b):
#     return a + b

# mul = lambda x,y:x*y

# print(reduce(sum, l))
# print(reduce(mul, l))

# practise set-13 
# 1

# 2
# name = input("Enter name: ")
# marks = int(input("Enter marks: "))
# phone = int(input("Phone number: "))

# s = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone)

# print(s)

# 3
# table = [str(7*i) for i in range(1, 11)]

# s = "\n".join(table)
# print(s)

# 4
# def divisible5(n):
#     if(n%5 == 0):
#         return True
#     return False

# a  = [1,2,34234,53,6234235,64343, 65,754,45,55]

# f = list(filter(divisible5, a))
# print(f)

# 5
# from functools import reduce
# l  = [111, 2, 65, 5553, 635, 65, 74, 45,55]


# def greater(a, b):
#     if (a>b):
#         return a 
#     return b

# print(reduce(greater, l))

# 6
# pip freeze > requirements.txt
# virtualenv harryenv

# 7
# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"
# app.run()

