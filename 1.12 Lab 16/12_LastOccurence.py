'''
[L16] Find Last occurrence of word
Given a string S and a word W, find the index of the last occurrence of the word W in the input string S.
Input:
    hello world hello
    hello
    where:
First line represents the input string S.
Second line represents the word W to be searched.
Output:
    12
Explanation:
Last occurence of 'hello' is at index 12.
'''
string = input(" ")
word = input(" ")
last_occurence = string.rfind(word)  #rfind() : this function returns a “-1” if a substring is not found rather than throwing the error.
print(last_occurence)