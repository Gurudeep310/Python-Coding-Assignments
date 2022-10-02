'''
[L15 P5] 1's complement
Given an integer N as input, find 1's complement of N.
Input:
    5
    where:
First line represents the value of N.
Output:
    2
Assumption:
Value of N can be in the range 0 to 10000.
'''
#https://www.youtube.com/watch?v=bcA-52W5vAk


N = int(input(" "))
rem = 0
quotient = N
N_copy = N
binary = []
while quotient!=0:
    quotient = N_copy// 2
    rem = N_copy % 2
    N_copy = quotient
    binary.append(rem)
number_of_bits = len(binary)
XOR_operation = 1<<number_of_bits
temp = (XOR_operation - 1)
ones_complement = N^temp
print(ones_complement)



