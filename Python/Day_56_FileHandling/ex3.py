
# r1 = open('Addfile1','r')
#
# print(r1.read())
# r1.close()
# Files are named location on disk to store information

# print(r1.readline())
# ValueError: I/O operation on closed file.


w2 = open('Addfile1','w')
w3 = w2.write(' started')
print(w3)
w2.close()