#RANDOM NUMBERS
#Random numbers can be generated in python and they can be generated in different ranges of your choice
#You use the randrange() function, which is available in the random module to generate random numbers
#To have the random module available, you need to import it first
import random

#now, call the randrange function on the module, and pass in two arguments
random.randrange(1,10) #the first and second numbers are the range you want the random number to be generated from

#You can get logical at this stage, for example, generating 3 digits number each time
random.randrange(100,999) #this will generate 3 digits random number each time

#INPUTS
#The input() function is used to allow others(including you) to provide data for a program you are coding
#Like how a calculator works, any user can provide any number without seeing the code working inside the calculator

#To collect a data, you use:
input() #Note that the input() function automatically collects data as strings

#You can further provide instructions to the user to let them know what sort of data you are expecting, like a name or number, etc.
#To do this, you pass your instruction as a string inside the the brackets
input('Please enter your name: ')

#You may store whatever the user provides by assigning it to a variable
variableName = input('Please enter your name: ')

#DATATYPE CONVERSION
#You can convert from one data type to another
#First you call the function representing the type you want to convert to
#Eample 1, converting from integer to float
float(2)

#You can convert, even if the data is assigned to a variable
number = 3.4
int(number) #converted to an integer

#converting from string to integer
figure = '245'
int(figure) #converted a number written as string to a real number, i.t an interger

#Yo can also converts values that are not directed assigned to a variable OR explicitly state, like the following
int(input('Enter a number of your choice: '))


#ASSIGNMENT 1
#Write a console application that collects two sets of numbers from a user
#Add the first and second number
#Then report the result of the addition like this: "number .... plus number .... is equal to ....."

#ASSIGNMENT 2
#Write a console application that greets someone
#Whatever name the user typed, it will say: "You are blessed ...."

#ASSIGNMENT 3
#Write a console application that generates random numbers in 6 digits (must always be 6 digits)
#Then say: "your OTP is ....""
