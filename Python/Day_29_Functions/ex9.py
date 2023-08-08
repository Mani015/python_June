# Work flowing
def Fun1(x,y):
    print('working 2')
    print('This is Fun1')
    def Fun2(z):
        sum_of = x + y
        product_of  = y*z
        print('working 4')
        print(sum_of,product_of)
    print('working 3')
    Fun2(3)
    print('stop 5')
print('start 1')
Fun1(2,4)

# start 1
# working 2
# This is Fun1
# working 3
# working 4
# 6 12
# working 5