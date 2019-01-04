"""Use Sublime Text 3, save it as Functions2.py"""
##encoding: utf-8""
_author_ = 'Josue Wuezo' #Set the author of the coding
#'def' is a reserve word in Python, that means:'define'
def my_function(cad, v=2):
	print(cad*v)
#after declare my_function, I need to excecute it:
#The "cad" will become 'Python'
my_function('Python')
#The "cad" will become 'Python' and the v will become 5
my_function('Python',5)
#Everything after the '*' will become a Tuple:
def my_function2(cad, v=2, *Anytext):
	print(cad*v)
#we will use a 'for' type of loop to roam the Tuple
	for gameofthrones in Anytext:
		print(gameofthrones*5)
#This will execute all my declared strings
my_function2('Python', 5,"Hi  ", "Bye  ","N   ",'strings'  )
#This will only execute the first print, I won't go into the for,
#because there aren't "data" for that "Anytext" variable
my_function2('Python  ',5)
#Execute in terminal



