'''
[L15 P4] Swap value of two numbers
Given two integers N1 and N2, interchange values of the variable and print it. 
Input 
    4
    10
Output 
    10 4 
'''
N1 = int(input())
N2 = int(input())
Temp = N1
N1 = N2
N2 = Temp
print(N1,N2)