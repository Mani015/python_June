# def f1():
#     for i in range(1,10):
#         yield i
# result=f1()
# for value in result:
#     print(value)

def f1():
    for i in range(10):
        yield i
result = f1()
print(result.__next__())
print(result.__next__())
print(result.__next__())
