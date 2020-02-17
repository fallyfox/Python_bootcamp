#CREATE A FILE
 
#using open('filename',mode)
file = open('m_file.txt', 'w')
#w mode: you can only write to file
#r mode: you write and read file
#a will append text to the end of the file
#x mode: will create a file only if the file doesn't exist 
#Assigning the operation to a variable enables us to call additional i/o functions on it

#WRITE TO A FILE
#To write to a file, call the write function on the variable and pass in the string which is the data you are writing
file.write('Fun to code with \n')

#READ DATA FROM A FILE
#open the file in 'r' mode
#assign the operation to a variable so that you can call functions on it
#call the read function on it, pass the operation inside a print function if you are not using jupiter notebook
#an argument passed inside read() represents the limit of character to be read
read_me = open('m_file.txt', 'r')
print(read_me.read())

