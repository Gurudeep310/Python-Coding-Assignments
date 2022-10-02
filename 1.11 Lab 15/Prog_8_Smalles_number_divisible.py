'''
[L15 P9] Smallest number with sum of digits as N and divisible by 10^N
Given a number N, find the smallest number such that the sum of its digits is N and it is divisible by 10N .
Input:
    5
    where:
First line represents the value of N.
Output:
    500000
Explanation: 500000 is the smallest number divisible by 105 and sum of digits as 5.
'''
# https://www.geeksforgeeks.org/smallest-number-sum-digits-n-divisible-10n/

N = int(input(" "))
print(end ="")
if N == 0:
    print("0",end ="")
elif N % 9 != 0:
    print(N % 9,end ="")
i = 1
while i <= N/9:
    print("9",end ="")
    i = i + 1
j = 1
for j in range(N):
    print("0",end ="")
 

