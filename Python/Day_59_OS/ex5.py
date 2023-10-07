
# Listing out Files and Directories with Python
# os.listdir() method in Python is used to get the list of all files and directories
# in the specified directory. If we don’t specify any directory,
# then the list of files and directories in the current working directory will be returned.


import os

list1 = os.listdir("C:\\Users\\Test\\Desktop\\Python")

# for i in list1:
#     print(i)

# PBE_sep27
# PFS-Aug21
# Python-10Am
# Python_11AM
# Python_12pm
# Python_Aug
# Python_Definations
# python_June




for i in range(len(list1)):
    print(i,'index of: ',list1[i])
# 0 index of:  PBE_sep27
# 1 index of:  PFS-Aug21
# 2 index of:  Python-10Am
# 3 index of:  Python_11AM
# 4 index of:  Python_12pm
# 5 index of:  Python_Aug
# 6 index of:  Python_Definations
# 7 index of:  python_June
