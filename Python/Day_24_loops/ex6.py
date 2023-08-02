# print 1st 10 odd numbers , using while loop

intial_value = 0
odd_numbers = 0


while odd_numbers<=10:
    if intial_value%2!=0:
        print('odd number :',intial_value)
        odd_numbers+=1  #odd_numbers = odd_numbers + 1
    intial_value+=1  #intial_value = intial_value + 1
print('loop complete')


# odd number : 1
# odd number : 3
# odd number : 5
# odd number : 7
# odd number : 9
# odd number : 11
# odd number : 13
# odd number : 15
# odd number : 17
# odd number : 19
# odd number : 21
# loop complete
