

# def New1(num1):
#     def New2(num2):
#         return 'sum of num1 + num2:', num1 + num2
#     print(New2(10))
# New1(5)
# ('sum of num1 + num2:', 15)


def New1(num1):
    def New2(num2):
        return 'sum of num1 + num2:', num1 + num2
    return New2(10)
print(New1(5))
# ('sum of num1 + num2:', 15)







