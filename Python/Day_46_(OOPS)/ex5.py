
# How to update the class_variable by using class


class Book(object):
    book_name = 'Classmate'
    book_pages = 200
    book_type = 'Plane'

print(Book.book_name,Book.book_type,Book.book_pages)
# Classmate Plane 200
print('Updating the class_variables by using class')
# syn: class_name.class_variable = New_value

Book.book_name = 'paper_grid'
Book.book_type = 'Small'
Book.book_pages = 150

# print(Book.book_name,Book.book_type,Book.book_pages)

# Updating the class_variables by using class
# paper_grid Small 150


# deleting the variablename:
# syn: del variablename

del Book.book_name
print(Book.book_name)
# AttributeError: type object 'Book' has no attribute 'book_name'

del Book.book_pages
print(Book.book_pages)