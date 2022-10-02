'''
[L16] Number Pattern - Square number pattern - 2
Given two integers N1 and N2, display the number pattern as described in output. 
Input:
    5
    5
    where:
First line represents the value of N1( number of rows ).
Second line represents the value of N2( number of columns ).
Output:
    5 5 5 5 5
    5 4 4 4 4
    5 4 3 3 3
    5 4 3 2 2
    5 4 3 2 1
'''
rows = int(input())
columns = int(input())
number = rows + 1
#number_copy = number
j = 0
flag = 0
count = 0
while j < columns:
    for i in range(rows):
        if flag <= count:
            number = number - 1
            flag = flag + 1
        if i == rows-1:
            print(number,end = "")
        else:
            print(number,end= " ")
    number = rows + 1
    flag = 0
    count = count + 1
    print("\r")
    j = j + 1



