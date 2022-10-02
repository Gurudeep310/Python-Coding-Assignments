'''
[L15 P7] Determine weather conditions based on temperature
Given an integer as an input, it represents the temperature in centigrade. Determine the weather conditions based on the temperature.
Temperature < 0 then print "Freezing weather".
Temperature 0 - 10 then print "Very cold weather".
Temperature 10 - 20 then print "Cold weather".
Temperature 20 - 30 then print "Normal in temperature".
Temperature 30 - 40 then print "Its Hot".
Temperature >= 40 then print "Its Very Hot".
Input:
    42
    where:
Input represents the temperature in centigrade.
Output:
    Its very hot
'''
n = int(input(" "))
if n < 0:
    print("Freezing weather")
elif n >= 0 and n < 10:
    print("Very cold weather")
elif n >= 10 and n < 20:
    print("Cold weather")
elif n >= 20 and n < 30:
    print("Normal in temperature")
elif n>=30 and n<40:
    print("Its hot")
else:
    print("Its very hot")