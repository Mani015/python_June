import keyword

# print(len(keyword.kwlist))
x = keyword.kwlist
# print(len(x))

# x = 'bjhdvmhjcvdsjvcudvkuvkdvcudvb'
# print(len(x))

# not is keyword
print(True)
# True
print(not(True))
# False

x1 = 3
y1 = 5
print(x1 > 3 and y1 < x1)
# False


print(x1 > 3 or y1 < x1 )

# False

print(x1 > 3 or y1 < x1 and x1 >= 10)
# False