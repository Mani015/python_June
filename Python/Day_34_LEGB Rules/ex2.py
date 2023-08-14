# Local scope: The names that you define in this scope are only available or visible to the code within the scope.


# local variable using within localscope


g1 = 10
# def Outer():
#     def Inner():
#         l1 = 'Sravani'
#         print('local variable:',l1)
#     Inner()
# Outer()
# local variable: Sravani


def Outer():
    def Inner():
        l1 = 'Sravani'
        # print('local variable:',l1)
    Inner()
    # print('local variable:', l1)
Outer()
# NameError: name 'l1' is not defined

#
# Using the LEGB Rule for Python Scope
# Python resolves names using the so-called LEGB rule, which is named after the Python scope for names. The letters in LEGB stand for Local, Enclosing, Global, and Built-in. Here’s a quick overview of what these terms mean:
#
# Local (or function) scope is the code block or body of any Python function or lambda expression. This Python scope contains the names that you define inside the function. These names will only be visible from the code of the function. It’s created at function call, not at function definition, so you’ll have as many different local scopes as function calls. This is true even if you call the same function multiple times, or recursively. Each call will result in a new local scope being created.
#
# Enclosing (or nonlocal) scope is a special scope that only exists for nested functions. If the local scope is an inner or nested function, then the enclosing scope is the scope of the outer or enclosing function. This scope contains the names that you define in the enclosing function. The names in the enclosing scope are visible from the code of the inner and enclosing functions.
#
# Global (or module) scope is the top-most scope in a Python program, script, or module. This Python scope contains all of the names that you define at the top level of a program or a module. Names in this Python scope are visible from everywhere in your code.
#
# Built-in scope is a special Python scope that’s created or loaded whenever you run a script or open an interactive session. This scope contains names such as keywords, functions, exceptions, and other attributes that are built into Python. Names in this Python scope are also available from everywhere in your code. It’s automatically loaded by Python when you run a program or script.
#
# The LEGB rule is a kind of name lookup procedure, which determines the order in which Python looks up names. For example, if you reference a given name, then Python will look that name up sequentially in the local, enclosing, global, and built-in scope. If the name exists, then you’ll get the first occurrence of it. Otherwise, you’ll get an error.