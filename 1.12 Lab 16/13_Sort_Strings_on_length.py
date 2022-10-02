'''
[L16] Sort strings based on length
Given a string, sort the words according to word's length. 
Input:
    Yellowish red Orange black
Output: 
    red black Orange Yellowish
Assumptions: 
The length of strings in the array is within the range [0 to 10000]. 
'''

def length(e):
    return len(e)

string = input(" ")
words = string.split(" ")
words.sort(reverse=True, key=length)
words.reverse()
for i in range(len(words)):
    print(words[i],end = " ")