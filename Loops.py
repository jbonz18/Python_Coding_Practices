##encoding: utf-8""
age = int(input("Write your age "))

while int(age) <= 50:
    #15 will be skipped
    if (age == 15):
    	age = age + 1
    	continue
    if (age == 31):
 #The process in the loop will end
        break 
    age = str(age)
    print ("You have: " + str(age))
    age = int(age) + 1
