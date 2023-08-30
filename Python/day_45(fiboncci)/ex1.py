def fib(n):
   a = 0
   b = 1
   if n == 1:
       print(a)
   elif n >= 2:
       print(a)
       print(b)
       for i in range(2, n):
           c = a + b   # 0 + 1 = 1
           a = b  # a = 1
           b = c  # b = 1
           print(b)

n = int(input("Enter the number: "))
fib(n)

# 0
# 1
# 1
# 2
# 3
# 5




