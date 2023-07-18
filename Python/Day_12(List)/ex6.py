
# insert()	Adds an element at the specified position

stu = ['swapnapriya','laxmi','jhansi','prasad','girish']

# syn:list.insert(position, value)

stu.insert(2,'priya')
print(stu)
# ['swapnapriya', 'laxmi', 'priya', 'jhansi', 'prasad', 'girish']
stu.insert(0,'sravanipriya')
print(stu)
# ['sravanipriya', 'swapnapriya', 'laxmi', 'priya', 'jhansi', 'prasad', 'girish']

stu.insert(1,'anusha')
print(stu)
# ['sravanipriya', 'anusha', 'swapnapriya', 'laxmi', 'priya', 'jhansi', 'prasad', 'girish']

stu.insert(-2,'subbaraju')
print(stu)
# ['sravanipriya', 'anusha', 'swapnapriya', 'laxmi', 'priya', 'jhansi', 'subbaraju', 'prasad', 'girish']