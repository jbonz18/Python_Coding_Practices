"""Use Sublime Text 3, save it as Functions3.py"""
##encoding: utf-8""
_author_ = 'Josue Wuezo' #Set the author of the coding
#Defining the function: ("Anytext" will become a "Dictionary", so we print 
#accordingly to its keywords)
def my_function(cad, v=2, **Anytext):
	print(cad*v)
	print(Anytext['extraString'])
	print(Anytext['anotherString'])
#Activation of the Function and assignation of Dictionary's keyword:
#(in this case, 'extraString' is the KeyWord of the first value of the Dictionary)
my_function('Python', 5,
extraString = '\nHello', 
anotherString ='\nBye')
