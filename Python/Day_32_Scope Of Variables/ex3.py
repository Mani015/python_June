# Adding the global variable and local variable

smile = 40
print('global variable:',smile)
def Angry():
    sad = 30
    print('global va:',smile)
    print('local va:',sad)
    life = smile + sad
    print('total life:',life)
Angry()
print('global va:',smile)
# global variable: 40
# global va: 40
# local va: 30
# total life: 70
# global va: 40

