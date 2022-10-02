'''
[L16] Fascinating Number
Given an integer N, find whether N is a Fascinating number or not. 
Display 1 if N is Fascinating number else 0. 
Input
    192 
Output
    1 
192 has 3 digits. Multiply it with 2 & 3 
192*2 = 384 
192*3 = 576 
Concatenated result = '192' + '384' + '576' = '192384576', which contains all digits from 1 to 9 exactly once. 
Assume that, 
N is an integer within the range [100 to 10000].
'''
# https://www.youtube.com/watch?v=YTOi9ZiVnXw

number = int(input())
num_mul_two = number * 2
num_mul_three = number * 3
new_number = str(number) + str(num_mul_two) + str(num_mul_three)
flag = 1
for i in range(1,10):
    fun = 0
    for j in range(len(new_number)):
        digit = new_number[j]
        if str(i) == digit:
            fun = fun + 1
    
    if fun != 1:
        flag = 0
        break
if flag == 1:
    print(1)
else:
    print(0)