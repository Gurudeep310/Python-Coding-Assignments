'''
[L17] Sort perfect squares in an list at their relative positions
Given an array of integers, write a program to sort only the elements which are Perfect squares at their relative positions in the array (positions of other elements must not be affected).
Input:
    6
    2 64 9 8 1 4
    where:
First line represents the number of elements in the list.
Second line represents the elements in the list.
Output:
    2 1 4 8 9 64
Explanation: 1, 4, 9 and 64 are the only perfect squares from the array. So only these elements are sorted, others are kept as they were in the input.
'''


import math

number = int(input())
string = input()
numbers = []
for word in string.split():
    if word.isdigit():
        numbers.append(word)
#print(numbers)

perfect_square = []
for i in range(len(numbers)):
    x = int(numbers[i])
    sqrt = math.sqrt(x)
    sqrt = int(sqrt)
    if (sqrt*sqrt) == x:
        perfect_square.append(x)
perfect_square.sort()
#print(perfect_square)

j = -1
for i in range(len(numbers)):
    x = int(numbers[i])
    sqrt = math.sqrt(x)
    sqrt = int(sqrt)
    if (sqrt*sqrt) == x:
        j = j + 1
        numbers[i] = perfect_square[j]
        #j = j + 1
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
    print(numbers[i],end = " ")
