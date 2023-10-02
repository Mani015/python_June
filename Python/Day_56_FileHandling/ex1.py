# import os
# print(os.getcwd())
# C:\Users\Test\PycharmProjects\pythonProject\Day_56_FileHandling

# What is File?
# Files are named location on disk to store information
# They are used to data permanently.
# Data is stored in non-volatile memory
# We  can retrived data whenever required


# Types of File
# Text File: Text file usually we use to store character data. For example, test.txt
# Binary File: The binary files are used to store binary data such as images, video files, audio files, etc.

# Create File in Python: You'll learn to create a file in the current directory or a specified directory.
#  Also, create a file with a date and time as its name. Finally, create a file with permissions.
# Create A Empty Text File
# We don’t have to import any module to create a new file. We can create a file using the built-in function open().

# syn: open(filename,mode)
# x		Open a file only for exclusive creation. If the file already exists, this operation fails.
New1 = open('Addfile1','x')
print(New1)
# <_io.TextIOWrapper name='Addfile1' mode='x' encoding='cp1252'>

# FileExistsError: [Errno 17] File exists: 'Addfile1'
