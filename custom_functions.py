#Creating a docstring(documentation) for your custom functions
#note: to find the docstring of a function, call the function with no arguments, then within the bracket press Shift and Tab
def product(num1,num2):
    """
    DOCSTRING
    Finds the product of two numbers
    --------
    Requires two positional arguments that must be integers or float
    """
    the_product = num1 * num2
    return the_product


#------------------------------------------------------------------------------------------------------


#Using function to retrieve information relating to different regions in Nigeria
def lagos():
    print("Lagos is the Nigeria's number 1 commercial city. Located in South-West")
def kano():
    print("Kano is known for commerce, mostly of local craft. Located in the North")
def ebonyi():
    print("Ebonyi produces the highest proportion of the nation's salt. Located in South-East")
    
state = input("Enter the region of your interest")
if state == "lagos":
    lagos()
elif state == "kano":
    kano()
elif state == "ebonyi":
    ebonyi()
else:
    print("This region is not available at this time.")

#---------------------------------------------------------
#Assignment
#---------------------------------------------------------
#Build a functional calculator that can perform all of these operations: addition, subtraction, multiplication and division
#Build each operation as a function
#Accept data from the user like the first number, math's operation sign(eg. +,-,*,/) and second number
#Write conditional statements to run specific block of code for each of the cases: (addition, subtraction, multiplication and division)
#Call the necessary function you had defined to carry our each operation and return the corresponding result within the conditional statements
#The result is expected to be in form of this example: 30 multiplied by 3 is equal to 90
#------------- end ---------------------------------------
