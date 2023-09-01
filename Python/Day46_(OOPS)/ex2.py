
# How to get the class variables.. by using class name
# syn: class_Name.Class_variable
class Pen(object):
    pen_name = 'Cello'
    pen_cost = 20
    pen_color = 'Black'
    pen_height = str(15)+'CM'

# ob1 = Pen()
# print(ob1)
# <__main__.Pen object at 0x000002639A2FC760>
# syn: class_Name.Class_variable
print(Pen.pen_name) # Cello
print(Pen.pen_color) # Black
print(Pen.pen_height) # 15CM
print(Pen.pen_cost) # 20

