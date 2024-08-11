# intro to loop
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# # The same task can be done like this:
# for i in range(1, 6):
#     print(i)

# while loop 
# i = 1

# while(i<51):
#     print(i)
#     i +=1 # or i = i + 1
# '''
# Output:
# 1
# 2
# 3
# 4
# 5
# '''

# list using while loop 
i = 1

# while(i<51):
#     print(i)
#     i +=1 # or i = i + 1
'''
Output:
1
2
3
4
5
'''
# for with else 
# l= [1,7,8] 

# for item in l:
#     print(item)

# else:
#     print("done") # this is printed when the loop exhausts!

#  break and continue 
# for i in range(100):
#     if(i == 34):
#         break # Exit the loop right now
#     print(i)

# for i in range(100):
#     if(i == 34):
#         continue # Skip this iteration
#     print(i)    

# pass keyword 
# for i in range(645):
#     pass

# i = 0
# while(i<45):
#     print(i)
#     i += 1



# practice set day-7
# 1
# num=int(input("enter a number:-"))
# print("table of given number is",num)
# for i in range(1,11):
#   print(f"{num} * {i} = {i*num}")

# 2
# l1=["Harry","Sohan","Sachin","Rahul"]
# for i in l1:
#   if(i[0]=="S"):
#     print(f"Hello {i}, nice to meet you")

# 3
# num=int(input("enter your number:-"))
# print("table of given number is",num)
# a=1
# while (a<=10):
#   print(f"{num} * {a} = {a*num}")
#   a+=1

# 4
# num=int(input("enter a number:-"))
# if (num==2):
#   print(f"{num} is a prime number")
# elif(num>2):
#   for i in range(2,num):
#     if ( num%i!=0):
#       print(f"{num} is a prime number")
#     else:
#       print(f"{num} is not a prime number")
# else:
#    print(f"{num} is not a prime number")