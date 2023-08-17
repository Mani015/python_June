# Global Keyword:
#
# In programming, the global keyword is often used to indicate that a variable
# declared within a function has a global scope, meaning it can be accessed and modified outside of the function's context.' \
# ' This keyword is particularly relevant in languages like Python.


l1 = [1,2,3]
print('before l1:',l1)

def Change_Outside():
    l2 = [4,5,6]
    print('local list:',l2)
    l1.extend(l2)
Change_Outside()
print('After list l1:',l1)
# before l1: [1, 2, 3]
# local list: [4, 5, 6]
# After list l1: [1, 2, 3, 4, 5, 6]
