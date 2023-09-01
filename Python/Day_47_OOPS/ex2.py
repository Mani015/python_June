class Watch(object):
    Brand_Name = 'Sonata'
    Brand_color = 'Glod'
    Brand_price = 3000
    def Display(self):  # self is  a current object
        print('I am a instance method')
# objectname = classname()
ob1 = Watch()
# Method calling
# syntax: objectname.Method_Name()
ob1.Display()
# I am a instance method

# Watch.Display(ob1)
