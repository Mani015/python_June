import time



localtime = time.localtime()
# # %%	It will return an actual "%" symbol.
# strftime means string from time
t1 = time.strftime("%A",localtime)
print(t1)
# Thursday



t2=time.strftime("%a",localtime)
print(t2)
# Thu