
# Dictionary deosn't allows duplicate keys

d1 = {'prasad':22,'laxmi':23,'priya':21,'sravani':24,'jhansi':21}
# print(d1)
# {'prasad': 22, 'laxmi': 23, 'priya': 21, 'sravani': 24, 'jhansi': 21}

# we are passing the duplicate key
d2 = {'prasad': 22, 'laxmi': 23, 'priya': 21, 'sravani': 24, 'jhansi': 21,'priya':25}
# print(d2)
# {'prasad': 22, 'laxmi': 23, 'priya': 25, 'sravani': 24, 'jhansi': 21}

# duplicate values

d3 = {'prasad': 22, 'laxmi': 23, 'priya': 25, 'sravani': 24, 'jhansi': 21,'anusha':23}
# print(d3)
# {'prasad': 22, 'laxmi': 23, 'priya': 25, 'sravani': 24, 'jhansi': 21, 'anusha': 23}

d4 = {'prasad': 22, 'laxmi': 22, 'priya': 22, 'sravani': 22, 'jhansi': 22, 'anusha': 22}
print(d4)
# {'prasad': 22, 'laxmi': 22, 'priya': 22, 'sravani': 22, 'jhansi': 22, 'anusha': 22}
