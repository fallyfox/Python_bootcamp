#location database
location = {'lagos':1300,'enugu':880,'maiduguri':1400,'calabar':940,'accra':1600,'cotonou':1500,'ibadan':720}
#value of 1 liter of fuel
fuel = 145
#value of driver trip per 30km
driver = 1000

print('Welcome to the Trip Profit Calculator')
dest_select = input('Enter your destination: \n')
bus_size = int(input('Enter bus sitting capacity: \n'))

#------- Cost calculation starts here -------------
distance = location[dest_select]
fuel_cost = (distance / 30) * fuel
driver_cost = (distance / 10) * driver
total_cost = fuel_cost + driver_cost
#------- cost calculation ends here ---------------

def your_result():
    revenue = bus_size * 9800
    profit = revenue - total_cost
    print(f"""
    Here is your trip summary
    --------------------------
    Destination: {dest_select}
    Fuel cost: {fuel_cost}
    Driver's fee: {driver_cost}
    TOTAL COST: {total_cost}
    
    Revenue: {revenue}
    
    PROFIT: {profit}
    ---------------------------
    """)
    
#------- profit calculation starts here -----------
if distance >= 700 and distance <= 1000:
    your_result()
elif distance >= 1001 and distance <= 1200:
    your_result()
elif distance > 1200:
    your_result()
else:
    print("An error was encountered")
