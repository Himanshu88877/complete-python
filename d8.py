# function in python 

# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
 
# average = (a + b + c)/3
# print(average)

# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# c = int(input("Enter your number: "))
 
# average = (a + b + c)/3
# print(average)

# Function Definition
# def avg():
#     a = int(input("Enter your number: "))
#     b = int(input("Enter your number: "))
#     c = int(input("Enter your number: "))
    
#     average = (a + b + c)/3
#     print(average)


# avg() # Function Call
# print("Thank you!")
# avg()
# print("Thank you!")
# avg()
# print("Thank you!")
# avg()
# avg()

# quize 
# def goodDay():
#     print("Good Day")

# goodDay()

# function with arguments 
# def goodDay(name, ending):
#     print("Good Day, " + name)
#     print(ending)
#     return "ok"

# a = goodDay("Harry", "Thank you") 
# print(a)

#  default arguments 
# def goodDay(name, ending="Thank you"):
#     print(f"Good Day, {name}")
#     print(ending)

# goodDay("Harry", "Thanks")
# goodDay("Rohan")

# recurssion
'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(n) = n X n-1 X......3 X 2 X 1

factorial(n) = n * factorial(n-1)
'''

# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n * factorial(n-1)


# n = int(input("Enter a number: "))
# print(f"The factorial of this number is: {factorial(n)}")

# practise set-8
# 1
# def greatest(a, b, c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>b and c>a):
#         return c

# a = 1
# b = 23
# c = 3

# print(greatest(a, b, c))

# 2
# def f_to_c(f):
#     return 5*(f-32)/9

# f = int(input("Enter temperature in F: "))
# c = f_to_c(f)
# print(f"{round(c, 2)}°C")

# 3
# print("a")
# print("b")
# print("c", end="")
# print("d", end=""), 

# 4
'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4.... n -1 + n
sum(n) = sum(n-1) + n
'''

# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n

# print(sum(4))

# 5
# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n-1)


# pattern(3)

# 6
# def inch_to_cms(inch):
#     return inch * 2.54

# n = int(input("Enter value in inches: "))

# print(f"The corresponding value in cms is {inch_to_cms(n)}")

# 7
# def rem(l, word):
#     n = [] 
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n


# l = ["Harry", "Rohan", "Shubham", "an"]

# print(rem(l, "an"))

# 8
# def multiply(n):
#     for i in range(1, 11):
#         print(f"{n} X {i} = {n*i}")

# multiply(5)

