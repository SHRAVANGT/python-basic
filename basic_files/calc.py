######################################
######################################
######################################
######################################
#
#
#
#
#here are some examples of functions of calculator
#
#######################################
#######################################


import sys # to use cmd line args


#a =10
#b= 10 #global variable

#x=addition(5 , 10) its static we are not getting input from users
#############we are using user input by cmd sys.argv[]  here [] specifies order of operation

print("first number is:")
a = float(input())
print("first number is:",a)
print("select operation")
print(" ")
print(" 1 - addition.\n  2 - subtraction.\n  3 - multiplication.\n  4 - exit ")
operation =int( input())
print("selected operation is:",operation)
print("second number:")
b = float(input())
print("second number:", b)
#print(x)
#y=subtraction(9 , 6)
#print(y)
#z=multiplication(3 ,4)
#print(z)

def addition(a , b):
	add = a+b
   # print("result of addition",add)  we can do other way
	return add  

def subtraction(a , b):
	sub=a-b
   # print("result of subtraction",sub)
	return sub

def multiplication(a , b):
	mul = a*b
    #print("result of multiplication",mul)
	return mul

#################
#we are using  condtions to execute functions

if operation == 4:
 print("not not")

else:
	if operation == 1:
	   x = addition(a , b)
	   print(x)
	elif operation == 2:
	   y = subtraction(a , b)
	   print(y)
	elif operation == 3:
	   z= multiplication(a , b)
	   print(z)
	else:
	     print("not found")
