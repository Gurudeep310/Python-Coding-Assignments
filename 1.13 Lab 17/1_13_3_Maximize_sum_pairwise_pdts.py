'''
[L17] Maximize sum of pairwise products in an list
Given an array of integers, find the maximum sum of pairwise multiplications. If there are an odd number of elements, then we can add anyone element (without forming a pair) to the sum.
Input:
    7
    -1 4 5 -7 -4 9 0
    where:
First line represents the number of elements in the list.
Second line represents the elements in the list.
Output:
    77
Explanation: So to get the maximum sum, the arrangement will be {-7, -4}, {-1, 0}, {9, 5} and {4}. So the answer is (-7 * (-4))+((-1) * 0)+(9 * 5)+(4) = 77.
Assumptions:
Array elements can be in the range -1000 to 1000.
'''

# https://stackoverflow.com/questions/42751063/python-filter-positive-and-negative-integers-from-string/42751169

import re

MOD= 1000000007
number = int(input())
string = input()
arr = [int(d) for d in re.findall(r'-?\d+',string)]   
'''
-?\d+ - matches positive and negative integers
Raw string notation (r"text") keeps regular expressions sane. Without it, every backslash ('\') in a regular expression would have to be prefixed with another one to escape it
'''
print(arr)        
n = len(arr)
sum = 0
arr.sort()
i = 0
while i < n and arr[i] < 0:
    if i != n - 1 and arr[i + 1] <= 0:
        sum = (sum + (arr[i] * arr[i + 1])% MOD) % MOD
        i = i + 2
    else:
        break

j = n - 1
while j >= 0 and arr[j] > 0:
    if j != 0 and arr[j - 1] > 0:
        sum = (sum + (arr[j] * arr[j - 1])% MOD) % MOD
        j -= 2
    else:
        break

if j > i:
    sum = (sum + (arr[i] * arr[j]) % MOD)% MOD
elif i == j:
    sum = (sum + arr[i]) % MOD
print(sum)