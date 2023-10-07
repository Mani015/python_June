
# Deleting Directory or Files using Python
# OS module proves different methods for removing directories and files in Python. These are –
#
# Using os.remove()
# Using os.rmdir()
# Using os.remove()
# os.remove() method in Python is used to remove or delete a file path. This method can not remove or delete a directory. If the specified path is a directory then OSError will be raised by the method.
#
import os

# rm = os.rmdir('C://Users//Test//PycharmProjects//pythonProject//Day_59_OS//jhnasi.txt')
# 
# print(rm)

os.remove('jhansi')
