'''
[L16] Number Pattern - Diamond number pattern - 1
Given an integer N, print number pattern as described in output. 
Input:
    5
    where:
First line represents the rows input N.
Output:
    1
    1 2
    1 2 3
    1 2 3 4  
    1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2     
    1
Assumptions:
N can be in the range 1 to 1000
'''

number = int(input())
count1 = 0
count2 = 0
for i in range(number+1):
    for j in range(i):
        if j == i - 1:
            print(j+1,end = "")
        else:
            print(j+1,end = " ")
    count1 = count1 + 1
    if count1 != 0:
        print("\r")

count = 1
count_copy = count
j = 0
i = 0
while number != 0:
    for i in range(number-1):
        if i == number-2:
            print(count_copy,end="")
        else:
            print(count_copy,end = " ")
            count_copy = count_copy + 1
        count2 = count2 + 1
    if count2 != number-2:
        print("\r")
    count_copy = count
    number = number - 1
    j = j + 1



