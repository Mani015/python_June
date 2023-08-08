
# Nested Function:
# A function iniside of another function is called Nestedfunction

def Fun1(x,y):
    print('This is Fun1')
    def Fun2(z):
        sum_of = x + y
        product_of  = y*z
        print(sum_of,product_of)
    Fun2(3)

Fun1(2,4)


# This is Fun1
# 6 12