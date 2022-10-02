'''
[L15 P5] Check whether the entered character is a vowel or consonant
Given a character C, check whether it is a vowel or consonant.
Vowels = { 'a', 'e', 'i', 'o', 'u' }
Consonants = { x | x ∉ Vowels }
Input:
   c
  where:
First line represents the entered character C.
Output:
    consonant
Explanation: 'c' is a consonant, hence the output "consonant".
Assumption:
Input character can be any letter in the English Alphabet.
'''
character = input(" ")
if character == 'a' or character == 'A':
    print("vowel")
elif character == 'e' or character == 'E' :
    print("vowel")
elif character == 'i' or character == 'I':
    print("vowel")
elif character == 'o' or character == 'O':
    print("vowel")
elif character == 'u' or character == 'U':
    print("vowel")
else:
    print("consonant")