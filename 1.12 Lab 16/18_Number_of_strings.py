'''
[L16] Number of substrings divisible by 6
Given a string S consisting of integers 0 to 9, find the number of substrings which are divisible by 6. Substring does not contain leading zeroes
Input:
    606
    where:
First line represents input string S.
Output:
     5
Explanation:
Substrings "6", "0", "6", "60", "606" are divisible by 6.
Input:
    4806 
Output:
     5
Explanation:
Substrings "0", "6", "48", "480", "4806" are divisible by 6.
'''

def fun(i, n, string, m):
    if (i == len(string)):
        return 0
    if (m[i][n] != -1): 
        return m[i][n] 
    x = ord(string[i]) - ord('0')
    answer = (((x + n) % 3 == 0 and x % 2 == 0) +
          fun(i + 1, (n + x) % 3, string, m)) 
    m[i][n] = answer
    return m[i][n]

string = input("")
length = len(string)
m = [[-1] * 3 for i in range(length + 1)]
answer = 0
for i in range(len(string)):
    if (string[i] == '0'):
        answer = answer + 1
    else:
        answer = answer + fun(i, 0, string, m)
print(answer)