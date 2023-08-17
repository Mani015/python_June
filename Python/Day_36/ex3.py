
# Without using global keyword
# g1 = 'girish'
# print('before global_var:',g1)
#
# def Name_Change():
#     g1 = 'GIRISH'
#     print('local var:',g1)
# Name_Change()
# print('After global var:',g1)
# before global_var: girish
# local var: GIRISH
# After global var: girish





# AFTER USING GLOBAL KEYWORD:
g1 = 'girish'
print('before global_var:',g1)

def Name_Change():
    global g1
    g1 = 'GIRISH'
    print('local var:',g1)
Name_Change()
print('After global var:',g1)

# before global_var: girish
# local var: GIRISH
# After global var: GIRISH











