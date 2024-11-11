#I have't used python mucb before so I'm moving my notes to this file!
First = 'Hello World'
#print(First)
#different variable types
integer = 2010
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
#loops and other things that use: care indentation sensitve!
#if can also be used to check if a bool is true.

#FOR LOOP
for i in range(3):
    print('recursion', i + 1)
print(range(3))
#range by itself could be nice for alphastat

#WHILE LOOP
loop = 0
while loop < 5:
    loop = loop + 1
    print(loop)
while True:
    #infinite loop
    user_input = input('Enter 0 to end!')
    if user_input == '0':
        print('0 entered!')
        break
    else:
        print('that aint 0')

#FUNCTIONS
#def is the keyword
def hello_name(name):
    print('Hey there ', name)

#We calling functions now!
hello_name('Username1')
hello_name('Username2')

#KEYWORD pass  allows for empty functions that are being worked on to not break the program while running
def gaming():
    pass
#Works exactly like id expect from Lua

#TRY & ACCEPT block
num = input("Input a number: ")
try:
    print(10 + int(num))
except:
    print('Invalid Number')
#Note python lets you name a variable 'int' which causes int to fail to convert strings to int