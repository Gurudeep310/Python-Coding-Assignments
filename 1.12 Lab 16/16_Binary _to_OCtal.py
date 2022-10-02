'''
[L16] Convert a binary number into octal
Given a binary number N, convert it into an octal number.
Input:
    1001
    where:
First line represents binary number N.
Output:
    11
'''
# https://codescracker.com/python/program/python-program-convert-binary-to-octal.htm

bnum = input()
onum = int(bnum, 2)
onum = oct(onum)
print(onum[2:])