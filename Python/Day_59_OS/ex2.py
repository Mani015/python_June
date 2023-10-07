
# Changing the Current working directory
#
# To change the current working directory(CWD) os.chdir() method is used.
# This method changes the CWD to a specified path.
# It only takes a single argument as a new directory path.

# chdir() : change directory(path)

import os

cd = os.chdir("C:\\Users\\Test\\Desktop\\Python\\Python_Definations")
print(cd)

# C:\Users\Test\Desktop\Python\Python_Definations
print(os.getcwd())
