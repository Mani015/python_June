
pic1 = open('flower.png','rb')
# print(pic1.read())

pic2 = open('lav.png','wb')

for i in pic1:
    print(pic2.write(i))

