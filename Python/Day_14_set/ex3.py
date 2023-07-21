
s1 = {1,2,3,4,5,6,7,'tata','mphasis','e&y','accenture','jpmorgan','pepejeans'}

s1.update({'wipro','wellsforgo','infosys'})
# print(s1)
# {1, 2, 3, 4, 5, 6, 7, 'accenture', 'mphasis', 'e&y', 'infosys', 'tata', 'pepejeans', 'jpmorgan', 'wipro', 'wellsforgo'}


# adding the single value:

s3 = {'laxmi','pasrad','anusha','padmapriya','sravanipriya'}

s3.add('girish')
print(s3)
# {'anusha', 'girish', 'padmapriya', 'pasrad', 'sravanipriya', 'laxmi'}

s3.add('Jhansi')
print(s3)
# {'padmapriya', 'laxmi', 'girish', 'Jhansi', 'anusha', 'pasrad', 'sravanipriya'}

s3.add('subbaraju','balaraju')
print(s3)
# TypeError: set.add() takes exactly one argument (2 given)
