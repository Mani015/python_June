import sys


print('interpreter capacity:',sys.getrecursionlimit())
# interpreter capacity: 1000


def Camera_1():
    print('Best ever camera')
    Camera_1()
Camera_1()

# # import sys
# # sys:The sys modules provieds accesss to the system specific parameter and function