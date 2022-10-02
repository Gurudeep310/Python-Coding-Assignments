'''
[L16] Number Pattern - Square number pattern - 1
Given two integers N1 and N2, display the given circle number pattern with 1's and 0's (Square number patterns).
Input:
    5
    5
    where:
First line represents the value of N1( number of rows ).
Second line represents the value of N2( number of columns ).
Output:
   0 1 1 1 0  
   1 0 0 0 1
   1 0 0 0 1
   1 0 0 0 1   
   0 1 1 1 0
'''
rows = int(input())
columns = int(input())
'''
j = 0
flag1 = 0
for i in range(rows-1):
    if i == 0:
        print(0,end=" ")
    else:
        print(1,end=" ")
    if i == rows-2:
        print(0,end="")
print("\r")
while j < columns-2:
    for i in range(rows-1):
        if i == 0:
            print(1,end = " ")
        else:
            print(0,end = " ")
        if i == rows-2:
            print(1,end = "")
    print("\r")
    j = j + 1
for i in range(rows-1):
    if i == 0:
        print(0,end=" ")
    else:
        print(1,end=" ")
    if i == rows-2:
        print(0,end="")
'''
for i in range(rows+1):
    if i<1:
        print(0,end =" ")
        for j in range(columns-2):
            print(1,end = " ")
        print(0)
    
    elif i > rows-1:
        print(0,end = " ")
        for j in range(columns-2):
            print(1,end = " ")
        print(0)

    elif i>1 and i<=(rows-1):
        print(1,end= " ")
        for j in range(columns-2):
            print(0,end = " ")
        print(1)

