'''
[L17] Longest palindromic substring
Given a string S, find the longest substring which is Palindrome.
Input:
    AllcodeaedocAll
    where:
First line represents the input string
Output:
    codeaedoc
Assumptions:
Length of the string S can be 0 to 10000
'''

# https://www.youtube.com/watch?v=TLaGwTnd3HY&t=272s
# https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/
# https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/

# A Python3 solution for longest palindrome
 
# Function to pra subString str[low..high]
def printSubStr(str, low, high):  
    for i in range(low, high + 1):
        print(str[i], end = "")
 
str = input()
n = len(str)
maxLength = 1  # All alphabets are a palendrome.
start = 0
for i in range(n):
    for j in range(i, n):
        flag = 1
        for k in range(0, ((j - i) // 2) + 1):  # Checks alphabet by alphabet is it a palendrome or not
            if (str[i + k] != str[j - k]):
                flag = 0
        if (flag != 0 and (j - i + 1) > maxLength):
            start = i
            maxLength = j - i + 1
                 
print("Longest palindrome subString is: ", end = "")
printSubStr(str, start, start + maxLength - 1)