# my_file = open('test.txt')
# print(my_file.read())
# print(my_file.readline()) #will only the first line
# print(my_file.readlines()) #will return all the lines in the text in a list.


# '''
# You can only read a file once using a cursor in reading a file.
# '''

# my_file.close()

#modes in files
'''
r - read
r+ - read and write (overwrites from the cursor not at the end)
w- write (creates a new file if that file does not exist)
a- this appends to the end of the file- better than r+ for writing more into the file.
'''

try:
    with open('texts/happy.txt', mode='r+') as my_file:
     text = my_file.write('):')
    print(text)
except FileNotFoundError as err:
   print("File does not exist")
   raise err
except IOError as err:
   print('IO error')
   raise err
#with this, you do not have to close the file everytime you open.

