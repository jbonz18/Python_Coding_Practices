#Dictionaries
#A type of Collection of Data, are the Dictionaries of Python. They had a different syntaxes,
#because their elements had a "keyword". Yes, we will define, our own "Reserved Keyword"
#in our programs. Dictionaries are also known as "Associative Matrixes" (like whe using jSon).
#The "keywords" are case sensitives.
d ={'Key1':[1,2,3],
    'Key2':True,
    'Key3':5,
    4: False
}
print (d)
print (d['Key2'])
print (d[4])
#In Dicitionaries, you can modify the value on a keyword at any moment; but once the keyword
#is declared, I can't modify the "keyword".
d[4] = True
print (d[4])
#You could also change the type of value keyword had:
d[4] = "Hello"
print (d[4])
#Arrays and Tuples are sequential lists, but the Dictionaries are not sequential; so we can't
#do "slicing", because they don't have indexes