
# with open('Addfile1','r') as file1:
#     print(file1.readlines())
# print('This file is closed:',file1.closed)
# print('File name is: ',file1.name)
# print('file mode is:',file1.mode)

# This file is closed: True
# File name is:  Addfile1
# file mode is: r


# How to read the first_line and last_line by using readline()

with open('Addfile1','r') as file:
    beginline = file.readline()#Read the first_line
    print(beginline)
    for endline in file:
        pass
    #Read the last_line
    print(endline)


