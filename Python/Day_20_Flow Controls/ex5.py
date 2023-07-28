
l1 = eval(input('Enter level one:'))

if l1==1:
    print('level_1 completed')
    l2 = int(input('Enter levelTwo:'))
    if l2 == 2:
        print('level_2 completed')
        l3 = int(input('Enter level three:'))
        if l3 == 3:
            print('level_3 completed')
        else:
            print('you are failed at level_3')
    else:
        print('you are fail at level_2')
else:
    print('you are fail at level_1')
