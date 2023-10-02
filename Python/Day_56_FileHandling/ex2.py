
# r1 = open('Addfile1','r')
# r2 = r1.read()
# print(r2)
# r1.close()
# w		Create a new file for writing. If a file already exists,
# it truncates the file first.
# Use to create and write content into a new file.

W1 = open('Addfile1','w')
w2 = W1.write('Files are named location on disk to store information')
print(w2)

W1.close()
# 53
r1 = open('Addfile1','r')
r2 = r1.read()
print(r2)
r1.close()


# Files are named location on disk to store information
