
# break	Terminate the current loop. Use the break statement to come out of the loop instantly.
# The break statement is used inside the loop to exit out of the loop.
# In Python, when a break statement is encountered inside a loop, the loop is immediately terminated,
# and the program control transfer to the next statement following the loop

# break

l1 = [1,2,3,4,5,6,7,8,9,10]

for i in l1:
    if i==6:
        break

    print(i)
print('Loop Terminated')
# 1
# 2
# 3
# 4
# 5
# Loop Terminated








