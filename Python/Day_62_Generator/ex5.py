
def f1():
    return 1
    return 2
    return 3
print(f1())
# generator is a function which contain yield keyword

def f2():
    yield 1
    yield 2
    yield 3
result=f2()
print(result.__next__())
print(result.__next__())
print(result.__next__())
print(result.__next__())


