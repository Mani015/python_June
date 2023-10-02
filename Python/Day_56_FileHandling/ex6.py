
# How to send the data from one file to another file

Read = open('Addfile1','r')

Newfile = open('Addfile2','w')

for i in Read:
    print(Newfile.write(i))

