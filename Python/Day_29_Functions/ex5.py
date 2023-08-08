# The statements after the return statements are not executed.

def Task():
    print('Statement_1')
    print('Statement_2')
    print('Statement_3')
    return 'statements completed'
    # print('Statements start')

print(Task())
# Statement_1
# Statement_2
# Statement_3
# statements completed
