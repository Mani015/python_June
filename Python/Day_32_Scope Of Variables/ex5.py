
# Enclosing Variable:

g1 = 'Prasad'
print('global v:',g1)

def First_Name():
    e1 = 'kumar'
    print('Enclosing variable:',e1)
    def Last_Name():
        l1 = 'kanchi'
        print('Local variable:',l1)
        FullName = g1 + e1 + l1
        return FullName
    print(Last_Name())
First_Name()
# global v: Prasad
# Enclosing variable: kumar
# Local variable: kanchi


# global v: Prasad
# Enclosing variable: kumar
# Local variable: kanchi
# Prasadkumarkanchi