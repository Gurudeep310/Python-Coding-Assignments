'''
Display the binary equivalent of a given decimal number
Given an integer N as input, display its binary equivalent.
Input:
    15
    where:
First line represents the integer N.
Output:
    1111
Explanation: N is displayed in its binary format.
'''

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
print(binary)
length = len(binary)
i = length - 1
while i>=0:
    print(binary[i],end = "")
    i = i - 1
