
# Returning Multiple Values: Although a function can only return one value directly, you can return multiple values as a tuple and unpack them at the caller's end.
# python
# Copy code
def calculate(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result

x,y = calculate(3, 5)

print(x)
print(y)