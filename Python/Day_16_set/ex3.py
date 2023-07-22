

# Using curly brackets: The dictionaries are created by enclosing the comma-separated Key: Value pairs inside the {} curly brackets. The colon ‘:‘ is used to separate the key and value in a pair.

# Using dict() constructor:  Create a dictionary by passing the comma-separated key: value pairs inside the dict().

# Using sequence having each item as a pair (key-value)


d1 = {'fname':'Jansi','Lname':'Rani','Address':'Kakinada','cellno':1234567890}
# print(d1)
# print(type(d1))
# {'fname': 'Jansi', 'Lname': 'Rani', 'Address': 'Kakinada', 'cellno': 1234567890}
# <class 'dict'>

# keys.
# syn: dictionary.keys()
print(d1.keys())
# dict_keys(['fname', 'Lname', 'Address', 'cellno'])

# values:
# syn: dictionary.values()
print(d1.values())
# dict_values(['Jansi', 'Rani', 'Kakinada', 1234567890])

# items:
print(d1.items())
# dict_items([('fname', 'Jansi'), ('Lname', 'Rani'), ('Address', 'Kakinada'), ('cellno', 1234567890)])
