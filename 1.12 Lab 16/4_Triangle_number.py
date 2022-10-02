'''
[L16] Number Pattern - Triangle number pattern - 2
Given an integer N, print odd number pattern as described in output. 
Input:
    5
    where:
First line represents the value of N.
Output:
    1 3 5 7 9
    3 5 7 9
    5 7 9
    7 9
    9
Assumptions:
N can be in the range 1 to 1000.
'''

number = int(input())
count = 1
count_copy = count
j = 0
i = 0
while number != 0:
    for i in range(number):
        if i == number-1:
            print(count_copy,end = "")
        else:
            print(count_copy,end = " ")
            count_copy = count_copy + 2
    print("\r")
    count = count + 2
    count_copy = count
    number = number - 1
    j = j + 1

