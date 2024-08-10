# intro to dictionary
# d = {} # Empty dictionary
# marks = {
#     "Harry": 100,
#     "Shubham": 56,
#     "Rohan": 23
# }
# # print(marks, type(marks))
# print(marks["Harry"])

# dictionary method 
# marks = {
#     "Harry": 100,
#     "Shubham": 56,
#     "Rohan": 23,
#     0: "Harry"
# }

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry": 99, "Renuka": 100})
# print(marks)
# print(marks.get("Harry2")) # Prints None
# print(marks["Harry2"]) # Returns an error

# intro to set 
# e = set() # Dont use s = {} as it will create an empty dictionary
# s = {1, 5, 32, 54,5, 5, 5} 
# print(s)

# set method 
# s = {1, 5, 32, 54,5, 5, 5, "Harry"}

# print(s, type(s))

# s.add(566)
# print(s, type(s))
# s.remove(1)
# print(s, type(s))

# s1 = {1, 45, 6, 78}  
# s2 = {7, 8, 1, 78}

# print(s1.union(s2))
# print(s1.intersection(s2))



# practice set of day 5
# 1
# dict1={
#   "kalam":"pen",
#   "kagaj":"page",
#   "subah":"morning"
# }
# inp=input("enter value from(kalam,kagaj,subah):-")
# print(dict1[inp])

# 2
# s=set()
# num1=int(input("enter a number:-"))
# num2=int(input("enter a number:-"))
# num3=int(input("enter a number:-"))
# num4=int(input("enter a number:-"))
# num5=int(input("enter a number:-"))
# num6=int(input("enter a number:-"))
# num7=int(input("enter a number:-"))
# num8=int(input("enter a number:-"))
# s.add(num1)
# s.add(num2)
# s.add(num3)
# s.add(num4)
# s.add(num5)
# s.add(num6)
# s.add(num7)
# s.add(num8)
# print(s)

# 3
# s1={18,"18"}
# print(type(s1))

# 4
# s=set()
# s.add(20)
# s.add("20")
# s.add(20.0)
# print(len(s))
# print(s)

# 5
# s={}
# print(type(s))

# 6
lang={}
name1=input("enter your name:-")
l1=input("enter your lang:-")

name2=input("enter your name:-")
l2=input("enter your lang:-")

name3=input("enter your name:-")
l3=input("enter your lang:-")

name4=input("enter your name:-")
l4=input("enter your lang:-")
lang.update({name1:l1})
lang.update({name2:l2})
lang.update({name3:l3})
lang.update({name4:l4})
print(lang)

# 7

