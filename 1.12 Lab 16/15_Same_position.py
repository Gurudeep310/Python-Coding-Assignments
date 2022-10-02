'''
[L16] Same position character as in English
Given a string S, find how many characters are in the same position as in English alphabets. 
Input: 
     AbcE1@rH 
Output: 
    4 
Here for the given string "AbcE1@rH", characters like A, b, c and H are at 1,2,3 and 8 positions respectively which is equal to their position in English alphabets. 
Assume that, 
Input string S is of length within a range [1 to 10000].
'''
'''
str = input(" ")
count = 0
for i in range(len(str)):
    if ((i == ord(str[i]) - ord('a')) or(i == ord(str[i]) - ord('A'))):
            count = count + 1
print(count)
'''
str = input(" ")
count = 0
for i in range(len(str)):
    if ((i == ord(str[i]) - ord('a')) or(i == ord(str[i]) - ord('A'))):
            count = count + 1
print(count)