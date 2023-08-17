def outer_function():
    outer_var = "I am from outer_function"
    def inner_function():
        nonlocal outer_var
        outer_var = "Modified in inner_function"
        print("Inner:", outer_var)
    inner_function()
    print("Outer:", outer_var)
outer_function()
# Inner: Modified in inner_function
# Outer: Modified in inner_function
