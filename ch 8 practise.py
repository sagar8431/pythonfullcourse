# factorial
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     return n*factorial(n-1)
# print(factorial(4))

# greatestof3
# def greatest(a,b,c):
#     if(a>b and a>c):
#         print("a is the greatest")
#     if(b>a and b>c):
#         print("b is greatest")
#     else:
#         print("c is the greatest")
# a=int(input("enter a"))
# b=int(input("enter b"))
# c=int(input("enter c"))
# greatest(a,b,c)

# farhenial to celcious
# def f_to_c(f):
#     return 5*(f-32)/9
# f=int(input("enter the temperature in f:"))
# print(f_to_c(f))

# Write a recursive function to calculate the sum of first n natural numbers. 
# def sum(n):
#     if(n==1):
#         return 1
#     else:
#         return sum(n-1)+n
# n=int(input("enter the no"))
# print(sum(n))

#  Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * 
# def number(n):
#     if(n==0):
#         return
#     print("*"* n)
#     number(n-1)
# number(3)


# 8. Write a python function to print multiplication table of a given number. 
# def multiply(n):
#     for i in range(1,11):
#         print(n ,"x", i ,"=", i*n)
# n=int(input("what table ypu want to print"))
# multiply(n)
