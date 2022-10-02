'''
Given an integer N, find whether the numbers is a magic number or not. 
Display 1 if N is magic number else 0. 
Input 
    199 
Output 
    1 
For 199, Sum of digits = 1 + 9 + 9 = 19, 
Sum of digits of 19 = 1 + 9 = 10 
Sum of digits of 10 = 1 + 0 = 1
'''

number = int(input(""))
if number % 9 == 1:
    print(1)
else:
    print(0)
