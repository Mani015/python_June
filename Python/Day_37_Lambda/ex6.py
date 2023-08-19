# Map with lambda
# syn: lambda arguments : expression
# syn : map(functionname,iterable)

print(list(map(lambda i : i+2,[1,2,3,4,5])))
# [3, 4, 5, 6, 7]

friends = ['ANUSHA','SRAVANI','JHANSI','GIRISH']
print(set(map(lambda name : name.lower(),friends)))
# {'jhansi', 'anusha', 'girish', 'sravani'}

