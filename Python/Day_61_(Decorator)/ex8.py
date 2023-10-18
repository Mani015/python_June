def Out_func(Fun):
    def In_func():
        New = Fun()  #<function Out_func.<locals>.In_func at 0x000002630DD821F0>
        return New.upper()
    return In_func

@Out_func
def New_Feature():  # New Functionality
    return 'python developer'

# PYTHON DEVELOPER

print(New_Feature())

@Out_func
def new_function():
    return 'This fucntion gives additionall feature'

# call this fucntion
print(new_function)  #<function Out_func.<locals>.In_func at 0x000001751D0C2430>
print(new_function())

# THIS FUCNTION GIVES ADDITIONALL FEATURE