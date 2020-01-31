#A tax deduction system. Deduction is based on company type. There 3 different taxes: VAT: 5%, IT: 15%, COP = 3%
#Applicable charges for different business types are as follows:
#1. enterprise: VAT: 5%
#2. company: VAT: 5% + IT: 15%
#3. corporation: VAT: 5% + IT: 15% + COP = 3%

#Business registration takes in business name, business type and revenue

print('Welcome to the online tax system')

#create a dictionary with default value for registration parameter
tax_manager = {
    #the integer 1, represents the default revenue
    'bus_name_rev':['business',1],
    'bus_type':['enterprise']
}

#change default parameters with user inputs
tax_manager['bus_name_rev'][0] = input('Enter your business name: ')
tax_manager['bus_name_rev'][1] = int(input('Enter your gross revenue: '))
tax_manager['bus_type'][0] = input('Enter your business type: ')

#retreive each parameter
bus_name = tax_manager['bus_name_rev'][0]
revenue = tax_manager['bus_name_rev'][1]
bus_type = tax_manager['bus_type'][0]

#calculate VAT at 5%
VAT = revenue * 0.05

if bus_type == 'corporation':
    COP = revenue * 0.03
    IT = revenue * 0.15
    sum_tax = COP + IT + VAT
    print(
    f"""
    Tax Summary for {bus_name}
    Business type: {bus_type}
    ------------------------------------
    Total revenue: {revenue}
    Tax: {sum_tax}
    """
    )
elif bus_type == 'company':
    IT = revenue * 0.15
    sum_tax = IT + VAT
    print(
    f"""
    Tax Summary for {bus_name}
    Business type: {bus_type}
    ------------------------------------
    Total revenue: {revenue}
    Tax: {sum_tax}
    """
    )
else:
    sum_tax = VAT
    print(
    f"""
    Tax Summary for {bus_name}
    Business type: {bus_type}
    ------------------------------------
    Total revenue: {revenue}
    Tax: {sum_tax}
    """
    )
