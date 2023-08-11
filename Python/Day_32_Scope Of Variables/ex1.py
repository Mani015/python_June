# Scope and Lifetime of Variables
# When we define a function with variables, then those variables’ scope is limited to that function.
# In Python, the scope of a variable is an area where a variable is declared. It is called the variable’s local scope.


# There are Four types of Scope of variables:
#
# 1).Local Variable scope
# 2).Global variable scope
# 3).Enclosing varaible scope
# 4).Built-in-Scope



# Local Variable in function
# A local variable is a variable declared inside the function that is not accessible from outside of the function.
# The scope of the local variable is limited to that function only where it is declared.
def Main_Func():
    loc_var = 20
    print('local variable:',loc_var)
Main_Func()
# local variable: 20
# If we try to access the local variable from the outside of the function,
# we will get the error as NameError.
# print(loc_var)
# NameError: name 'loc_var' is not defined