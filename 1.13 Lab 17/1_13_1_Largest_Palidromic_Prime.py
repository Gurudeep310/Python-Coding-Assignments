'''
[L17] Largest Palindromic prime
Given an array of integers, find the largest Palindromic Prime from the array.
If no element from the array is a Palindromic Prime then print -1.
Input:
    5
    11 5 121 7 89
    where:
First line represents the number of elements in the array.
Second line represents the elements in the array.
Output:
    11
Explanation: 11, 5 and 7 are the only Palindromic Primes from the array. 11 is the maximum among them.
'''
# https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
# https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
# https://www.kite.com/python/answers/how-to-extract-integers-from-a-string-in-python


import numpy as np


def reverse(x):         # Helps to reverse the string 34 to 43
    str = ""
    for i in x:
        str = i + str
    return str

def main():
    number = int(input())
    string = input()
    numbers = []
    '''
    for i in range(number):
        num = int(input())
        numbers.append(str(num))
    #print(numbers)
    '''
    for word in string.split():
        if word.isdigit():
            numbers.append(word)

    #print(numbers)
    
    all_palendromic_numbers = []
    for i in range(len(numbers)):
        x = numbers[i]
        y = reverse(x)
        if int(x) == int(y):
            all_palendromic_numbers.append(int(x))
    #print(all_palendromic_numbers)

    prime_numbers = []
    for i in range(len(all_palendromic_numbers)):
        flag = 0
        num = int(all_palendromic_numbers[i])
        if num > 1:
            for i in range(2,int(num/2)+1):
                if num%i == 0:
                    flag = 0
                    break
                else:
                    flag = 1
        else:
            flag = 0
        if flag == 1:
            prime_numbers.append(num)
    
    #print(prime_numbers)
    print(max(prime_numbers))
  
if __name__ == '__main__':
    main()
