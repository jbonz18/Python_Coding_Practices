"""Use Sublime Text 3, save it as Functions1.py"""
##encoding: utf-8""
_author_ = 'Josue Wuezo'
#Set the author of the coding
#'def' is a reserve word in Python, that means:'define'
def my_function(num1 = 0 , num2 = 0):
	print(num1+num2)
#after declare my_function, I need to execue it
my_function()
#the "num1" will become 3
my_function(3)
#the "num1" will become 3 and the "num2" will become 4
my_function(3,4)
#same example, but asking the user the numbers:
num1=int(input("Write a number: "))
num2=int(input("write a number: "))
my_function(num1,num2)
#execute in terminal

