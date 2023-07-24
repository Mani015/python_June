# get()	Returns the value of the specified key

dc1 = {'Realme':20000,'vivo':18000,'samsung':12000,'oppo':12000,'iphone':100000,'oneplus':30000}
# syntax: dictionary.get(key)
print(dc1.get('iphone'))
# 100000
print(dc1.get('vivo'))
# 18000
print(dc1.get('Realme'))
# 20000
# ---------------------------------------------------------
print(dc1['oppo'])
# 12000

print(dc1['samsung'],dc1['oneplus'])
# 12000 30000


