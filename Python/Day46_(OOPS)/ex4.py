
# How to update the class_variable by using object


class Book(object):
    book_name = 'Classmate'
    book_pages = 200
    book_type = 'Plane'

obj2 = Book()
print('B_Name:',obj2.book_name)
print('B_Pages:',obj2.book_pages)
print('B_Type:',obj2.book_type)

# B_Name: Classmate
# B_Pages: 200
# B_Type: Plane

# update the class variable value using object
# syn: object_name.class_variable = new_value

print('After updating the class variables:')
obj2.book_type = 'Broad lines'
# print('B_Type:',obj2.book_type)

obj2.book_pages = 500
obj2.book_name = 'Camel'

print('B_Name:',obj2.book_name)
print('B_Pages:',obj2.book_pages)
print('B_Type:',obj2.book_type)


# After updating the class variables:
# B_Name: Camel
# B_Pages: 500
# B_Type: Broad lines

