
# Creating a Directory
# There are different methods available in the OS module for creating a directory.

# os.mkdir()
# makedirectory

# Using os.mkdir()
# os.mkdir() method in Python is used to create a directory named path with the specified numeric mode.
# This method raises FileExistsError if the directory to be created already exists.
import os
# print(os.getcwd())
# nd = os.mkdir('jhnasi.txt')
# print(nd)


cd = os.chdir("C:\\Users\\Test\\Desktop\\Python\\Python_Definations")

mk = os.mkdir("C:\\Users\\Test\\Desktop\\Python\\Python_Definations\\osmodule")
print(mk)