
import sys
# Set the recurusion limit:
sys.setrecursionlimit(5)
def Employee():
    print('you are working very well')
    Employee()
Employee()



 # reason for display upto 966---the main problem is stack overflow and the memory utiliztion
# -------------------------------------------------------------------------------------------------
#  the maximum recursion depth that Python can handle depends on the available memory
# and the size of the call stack. In some cases, the recursion limit of 1000 may be
# reached before the call stack is full, resulting in a stack overflow error.
#
# In your specific case, the recursion limit of 1000 was reached before the call stack
# was completely filled, allowing Python to display up to 966 iterations. The exact
# number of iterations that can be displayed may vary depending on the factors mentioned above.
# ----------------------------------------------------------------------------------------------

