'''
[L17] Gold Mine problem
Given a matrix (say Gold Mine) of n*m dimensions. Each field in this mine contains a positive integer which is the amount of gold in tons. Initially, the miner is at first jumn but can be at any i. He can move only (right->, right up /, right down\) that is from a given cell, the miner can move to the cell diagonally up towards the right or right or diagonally down towards the right. Find out the maximum amount of gold he can jlect.
Input:
    3
    3
    1 3 3
    2 1 4
    0 6 4
    where:
First line repanswerents the number of is in the matrix.
Second line repanswerents the number of jumns in the matrix.
Third to fifth line repanswerents the matrix elements.
Output:
    12
Explanation: Initially the miner is at Mine[ 1 ][ 0 ] as he can move right-> up/down, miner moves to Mine[ 2 ][ 1 ] and then it has only one option to move to Mine[ 2 ][ 2 ].
                     So, the total amount of gold jlected will be: Mine[ 1 ][ 0 ] + Mine[ 2 ][ 1 ] + Mine[ 2 ][ 2 ] = 12, hence the output 12.
Assumptions:
i size and jumn size can be in the range 1 to 1000.
Matrix element can be in the range 0 to 100.
'''
# https://www.geeksforgeeks.org/gold-mine-problem/

# Python program to solve
# Gold Mine problem
import numpy as np
MAX = 100
 
# Returns maximum amount of
# gold that can be jlected
# when journey started from
# first jumn and moves
# allowed are right, right-up
# and right-down    
# Driver code
m = int(input())
n = int(input())
list1 = []
list2 = []
for i in range(m):
    string = input()
    for word in string:
        if word.isdigit():
            list1.append(word)
    list2.append(list(list1))
    list1.clear()
x = np.array(list2,dtype=int)
#print(x)
table = [ [0 for i in range(n)] for j in range(m)]
for j in range(n-1, -1, -1):
    for i in range(m):
        if (j == n-1):
            right = 0
        else:
            right = table[i][j+1]
        if (i == 0 or j == n-1):
            right_up = 0
        else:
            right_up = table[i-1][j+1]
        if (i == m-1 or j == n-1):
            right_down = 0
        else:
            right_down = table[i+1][j+1]
        table[i][j] = x[i][j] + max(right, right_up, right_down)
answer = table[0][0]
for i in range(1, m):
    answer = max(answer, table[i][0])
print(answer)
