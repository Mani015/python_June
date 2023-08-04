a=int(input("new number:"))
b=int(input("interest rate:"))
c=int(input("years:"))



x=0
while x<c:
    a+=a*b/100
    x+=1

    print("new number"+str(c)+"year"+str(a))

# new number:40
# interest rate:2
# years:1
# new number1year40.8
