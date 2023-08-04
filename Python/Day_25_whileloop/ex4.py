# num=int(input("enter number:"))
# count=0
# while num!=0:
#     num=num//10
#     # print("number is",num)
#     count = count * 10 + num
# print(num)

# Find out Prime number:

num = int(input('Enter one number:'))
Intial = 0
for i in range(1,num+1):
    if num%i==0:
        Intial+=1
if Intial==2:
    print('Prime number')
else:
    print('Not a Prime number')

# Enter one number:7
# Prime number
