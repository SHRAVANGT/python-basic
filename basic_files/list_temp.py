#
#
#
#
#######################
#######################
##
#
#this is example of lists and tuples
##
#
# now this file about searching and printing files from folders
#
##
##########################
#name =[1,2,3,4,54,5,566]
#list = ["name", "number" , 12 ,1 ]
#tuple = ("cat","dog", 33 ,5 )

#print(list)
#print(tuple)

#for i in name:

#print(i)
import os #to know about directory

print("enter the input")
a = (input("any elements").split())  #input takes input from user in runtime and split converts when elements with spaces to list
for folder in a:
	files=os.listdir(folder)
	print(files)
