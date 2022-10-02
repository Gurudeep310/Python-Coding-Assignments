'''
[L16] Number Pattern - Diamond number pattern - 2
Given an integer N, display the number pattern as described in output. 
Input:
    5
    where:
First line represents the value of N.
Output:
    1
    1 2 3
    1 2 3 4 5
    1 2 3 4 5 6 7
    1 2 3 4 5 6 7 8 9
    1 2 3 4 5 6 7
    1 2 3 4 5
    1 2 3
    1
'''
number = int(input())
count1 = 0
count2 = 0
i = 0
i_copy = i
while i < number:
    for j in range(i_copy+1):
        if j == i_copy:
            print(j+1,end = "")
        else:
            print(j+1,end = " ")
    count1 = count1 + 1
    if count1 != 0:
        print("\r")
    i_copy = i_copy + 2
    i = i + 1
#i_copy = i_copy - 1 # 9
count = 1
count_copy = count
j = 0
i = 0
while i_copy != 0:
    for i in range(i_copy-3):
        if i == i_copy-4:
            print(count_copy,end="")
        else:
            print(count_copy,end = " ")
            count_copy = count_copy + 1
        count2 = count2 + 1
    if count2 != i_copy-1:
        print("\r")
    count_copy = count
    i_copy = i_copy - 2
    j = j + 1
