'''
[L16] Number Pattern - Diamond number pattern - 3
Given an integer N, display the number pattern as described in output. 

 

Input:

    5

 

    where:

First line represents the value of N.
 

Output:

    0

    2 2 2

    0 0 0 0 0

    4 4 4 4 4 4 4

    0 0 0 0 0 0 0 0 0

    4 4 4 4 4 4 4

    0 0 0 0 0

    2 2 2

    0
'''
number = int(input())
count1 = 0
count2 = 0
i = 0
i_copy = i
n = 0
flag = 0
while i < number:
    for j in range(i_copy+1):
        if (i+1)%2 !=0:
            if j == i_copy:
                print(0,end = "")
            else:
                print(0,end = " ")
        else:
            if flag == 0:
                n = n + 2
            if j == i_copy:
                print(n,end = "")
            else:
                print(n,end = " ")
        flag = flag + 1
    flag = 0  
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
n = n + 2
flag1 = 0
number = number + 1
while i_copy != 0:
    for i in range(i_copy-3):
        if number%2 == 0:
            if flag1 == 0:
                n = n - 2
            if i == i_copy-4:
                print(n,end="")
            else:
                print(n,end = " ")
        else:
            if i == i_copy-4:
                print(0,end="")
            else:
                print(0,end = " ")
        flag1 = flag1 + 1  
        count2 = count2 + 1
    flag1 = 0
    if count2 != i_copy-1:
        print("\r")
    number = number + 1
    count_copy = count
    i_copy = i_copy - 2
    j = j + 1
