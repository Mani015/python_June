
g1 = 10
print('global var:' ,g1)  # 10
def Outer():
    global g1
    g2 = 20
    g1 = g2
    print('Enclosing var:' ,g2  )  # 20
    print('global var:', g1  )  # 10
    def Inner():
        nonlocal g2
        g2 = 30
        print('local vari:' ,g2  )  # 30
        print('global var:', g1  )  # 10
    print('Enclosing var:', g2)  # 20
    Inner()
    print('Enclosing var:', g2  )# 30
Outer()

# global var: 10
# Enclosing var: 20
# global var: 20
# Enclosing var: 20
# local vari: 30
# global var: 20
# Enclosing var: 30