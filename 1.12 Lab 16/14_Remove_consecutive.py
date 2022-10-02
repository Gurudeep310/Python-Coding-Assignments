'''
[L16] Remove consecutive repeated characters from string
Given a string S, Write a program to remove consecutive repeated characters from the string S.
Input:    
    aaaabbbbcccc
    where:
First line represents the input string S.
Output:
    abc
'''
def remDup(string):       
    length = len(string)
    if (length < 2) :
        return
    j = 0
    for i in range(length):
        if (string[j] != string[i]):
            j = j + 1
            string[j] = string[i]
    j = j + 1
    string = string[:j]
    return string

if __name__ == '__main__':
         
    string = input()
    string = list(string.rstrip())
    k = remDup(string)
    print(*k, sep = "")

