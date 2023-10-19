
# using return keyword
# def Square():
#     var = 0
#     num = 0
#     while var<=10:
#         New = num **2
#         var = var+1
#         num = num+1
#         return New
# print(Square())
#0


# Using yield keyword

def Square():
    var = 0
    num = 0
    while var<10:
        New = num ** 2
        print('Iterates:', New)
        yield New
        var+=1
        num+=1
x1 = Square()

for i in x1:
    print(i)
# Iterates: 0
# 0
# Iterates: 1
# 1
# Iterates: 4
# 4
# Iterates: 9
# 9
# Iterates: 16
# 16
# Iterates: 25
# 25
# Iterates: 36
# 36
# Iterates: 49
# 49
# Iterates: 64
# 64
# Iterates: 81
# 81