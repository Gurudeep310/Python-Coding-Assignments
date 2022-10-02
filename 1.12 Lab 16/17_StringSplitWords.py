'''
[L16] Split string by space into words
Given a string S, Write a program to split the string into words.
Input:
    How are you
    where:
First line represents the input string
Output:
    How
    are
    you
Assumptions:
Length of the string S can be 0 to 10000
'''

try:
    string = input(" ")
    words = string.split(" ")
    for i in range(len(words)):
        print(words[i])
except EOFError:
    '''Nothing'''