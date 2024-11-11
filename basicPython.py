#I have't used python mucb before so I'm moving my notes to this file!
First = 'Hello World'
#print(First)
#different variable types
int = 2010
#print(int )
string = 'bird is the word'
#print(string )
boollean = False
#print(boollean )
list = ['Luigi','Mario']
#print(list )
#to print an integer and a string together int needs to be converted to string
print (string + " " + str(int))
# same but reversed if you have a string with a number use int()

#BASIC OPERATORS
a = 5
b = 4
add = a + b
sub = a - b
mult = a * b
div = a / b
exp = a**b
print ("Basic Operators " + str(add) +" "+ str(sub) +" "+  str(mult) +" "+  str(div) +" "+  str(exp))

#LOGIC
if a > b:
    print(str(a) + " is greater than " + str(b))
else: 
    print(str(b) + " is greater than " + str(a))

#if can also be used to check if a bool is true.

    #FOR LOOP
for i in range(3):
    print('recursion', i + 1)
print(range(3))