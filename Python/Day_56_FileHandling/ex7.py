# readlines()	The readlines() method returns a list of lines from the file.
# using with

with open('Addfile1','r') as file1:
    print(file1.readlines())
print('This file is closed:',file1.closed)
# True
# [' started Greenish makes birds gly to flee \n', ' Lack of money is the root of all evil Greenish makes birds gly to flee \n', ' Lack of money is the root of all evil\n', ' life is full of suprises Marvels\n', 'win or lose keep trying\n', 'time is moneymoney is timei love you jesus']


f1 = open('Addfile1','r')
# print(f1.readlines())
# print('This file is closed:',f1.closed)
# This file is closed: False

