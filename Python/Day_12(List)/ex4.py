x1 = ['hyd','vijayawada','kakinada','tirupathi','vizag','ananthapuram','kuchipoodi','Rajamandry']

print(x1)

# ['hyd', 'vijayawada', 'kakinada', 'tirupathi', 'vizag', 'ananthapuram', 'kuchipoodi', 'Rajamandry']
# remove()	Removes the item with the specified value

x1.remove('vizag')
print(x1)
# ['hyd', 'vijayawada', 'kakinada', 'tirupathi', 'ananthapuram', 'kuchipoodi', 'Rajamandry']

x1.remove('tirupathi')
print(x1)
# ['hyd', 'vijayawada', 'kakinada', 'ananthapuram', 'kuchipoodi', 'Rajamandry']

# x1.remove()
# print(x1)
# TypeError: list.remove() takes exactly one argument (0 given)


x1.remove('kakinada','hyd')
print(x1)
# TypeError: list.remove() takes exactly one argument (2 given)


