'''
[L16] Disarium Number
Given an integer N, find whether N is a Disarium or not. 
Display 1 if N is Disarium number else 0. 
Input 
    135 
Output 
    1 
For 135, sum of digits powered with their respective position = 11 + 32 + 53 = 135, which is equal to an original number. 
'''
import math
number = input(" ")
list1 = []
list2 = []
for i in range(len(number)):
    list1.append(int(number[i]))
#print(list1)
for i in range(len(list1)):
    list2.insert(i,math.pow(list1[i],i+1))
sum = 0
#print(list2)
for i in range(len(list2)):
    sum = sum + list2[i]
#print(sum)
if sum == int(number):
    print(1)
else:
    print(0)