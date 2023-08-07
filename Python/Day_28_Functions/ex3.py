# How does it working

def Basic_Fucntion():
    print('this is used to code reusability')
    print('Function working End')

# print('Function working start:')
# Basic_Fucntion()


# Function working start:
# this is used to code reusability
# Function working End

# syn:
# def Addition(parameter1,parametrt2,....parameter_N):
#     statement....1
#     statement....2
#     statement..N
# Addition(Agruments1,Argumnts2,Arguments_N)


def Basic_Addition(x,y):
    z = x + y
    print('Addition of :',z)

# Basic_Addition()
# TypeError: Basic_Addition() missing 2 required positional arguments: 'x' and 'y'

# Basic_Addition(2)
# TypeError: Basic_Addition() missing 1 required positional argument: 'y'

# Passing the Arguments
Basic_Addition(2,3)
#5

