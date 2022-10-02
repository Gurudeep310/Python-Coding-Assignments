'''
[L16] Number Pattern - Triangle number pattern - 1
Given an integer N, display the number pattern as described in output. 
Input:
   5
    where:
First line represents the value of N( number of rows ).
Output:
    1
    2 1
    3 2 1
    4 3 2 1
    5 4 3 2 1
'''
number = int(input())
i = 0
n = 1
n_copy = n
while i <= number:
    for j in range(i):
        if j == i -1:
            print(n_copy,end="")
            n_copy = n_copy - 1
            
        else:
            print(n_copy,end=" ")
            n_copy = n_copy -1
            
    n_copy = n
    n = n + 1
    print("\r")
    i = i + 1