'''
[L15 P8] Find all factors of a number
Given numbers N, find all factors of it.
Input:
    12
    where:
First line represents value of N.
Output:
    1 2 3 4 6 12
Assumptions:
N can be in the range 1 to 100000.
'''
n = int(input(" "))
count = 1
while count <= n:
    if n%count == 0:
        print(count,end=' ') #end helps to print everything in horizontal line
    count = count + 1