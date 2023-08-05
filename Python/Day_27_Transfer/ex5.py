x = [1,2,3,4,5,6,7]
y = []

for i in x:
      if i & 2:
          continue
      y.append(i)
# print(y)
# [1, 4, 5]


# Find out the average of  divisible by 5 (from 1 to 100)
# First we take range(1,100)
sum = 0 # Intial Sum
count = 0 #This count no.of iterations

for i in range(1,100):
    if i%5==0:
        sum = sum+i
        count+=1
sum_of_deviations = sum
print('Total sum is :',sum_of_deviations)
No_of_Deviations = count
print('No. of Iterations:',No_of_Deviations)

Average = sum_of_deviations//No_of_Deviations
print('Total Average of :',Average)
# Total sum is : 950
# No. of Iterations: 19
# Total Average of : 50



