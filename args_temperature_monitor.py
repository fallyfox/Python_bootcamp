#import statistics module in order to use the stdev() function
import statistics

#define a function to accept unlimited arguments using *args
def temp_change(*args):
    
    #run stdev on the passed in arguments
    change = statistics.stdev(args)
    
    if change > 5:
        #do this if Standard Deviation is greater than 5
        print(f'Temperature change is: {change} \nAbnormal temperatures')
    else:
        #do this if Standard Deviation is less than 5
        print(f'Temperature change is: {change} \nNormal temperatures')

#call function and pass in unlimited temperatures as arguments
temp_change(53,52,54,56,65)
