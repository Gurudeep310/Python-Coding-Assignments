'''
[L15 P11] Swap the first and last digit of a number
Given a number N, swap the first and last digit of N using a loop.
Input:
    12345
    where:
First line represents value of N.
Output:
    52341
Assumptions:
N can be in the range 10 to 100000.
Number of digits in N is greater than 1.
'''
number = int(input(" "))
number_copy = str(number)
length = len(number_copy)
first_number = number_copy[0]
last_number = number_copy[length-1]
remaining = number_copy[1:length-1]
print(str(last_number) + str(remaining) + str(first_number))
