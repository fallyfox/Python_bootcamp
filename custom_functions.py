#Creating a docstring(documentation) for your custom functions
#NOTE: to find the docstring of a function, call the function with no arguments, then within the bracket press Shift and Tab
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
