
# difference()	Returns a set containing the difference between two or more sets

x1 = {'pandu','nani','chitti','bujji','bangaram','babe','bunny','munni','chunni'}

x2 = {'potti','bondam','laddu','cutie'}

print(x1.difference(x2))
# {'pandu', 'nani', 'bujji', 'chitti', 'bunny', 'bangaram', 'munni', 'chunni', 'babe'}

print(x2.difference(x1))
# {'cutie', 'laddu', 'potti', 'bondam'}

x1.update({'bondam','laddu'})
print(x1)
# {'bujji', 'bunny', 'laddu', 'bangaram', 'nani', 'munni', 'pandu', 'chunni', 'bondam', 'chitti', 'babe'}


print(x2.difference(x1))
# {'potti', 'cutie'}
