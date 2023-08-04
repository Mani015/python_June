num=int(input("enter number:"))
count=0
while num!=0:
    num=num//10
    print("number is",num)
    count+=1
print("number of digit given number is/count",count)
# enter number:22334455
# number is 2233445
# number is 223344
# number is 22334
# number is 2233
# number is 223
# number is 22
# number is 2
# number is 0
# number of digit given number is/count 8
