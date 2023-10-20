# Nickname Generator

# Write a function, nicknameGenerator that takes a string name as an argument and returns the first 3 or 4 letters as a nickname.

# If the 3rd letter is a consonant, return the first 3 letters.


# nickname("Robert") //=> "Rob"
# nickname("Kimberly") //=> "Kim"
# nickname("Samantha") //=> "Sam"
# If the 3rd letter is a vowel, return the first 4 letters.

# nickname("Jeannie") //=> "Jean"
# nickname("Douglas") //=> "Doug"
# nickname("Gregory") //=> "Greg"
# If the string is less than 4 characters, return "Error: Name too short".

# Notes:

# Vowels are "aeiou", so discount the letter "y".
# Input will always be a string.
# Input will always have the first letter capitalised and the rest lowercase (e.g. Sam).

#Understand 
#Input is a string of a name that will be title case
#Output is a string of either 3 or 4 letters based on if the original strings 3rd letter is a constant or a vowel
#Output will also include an error if name is less than 4 characters

#Plan

def sol(s):
    if len(s) < 4:
        return "Error: Name too short"
    if s[2] in 'aeiou':
        return s[:4]
    else: 
        return s[:3]

def nickname(s):
    v = 'aeiou'
    return 'Error: Name too short' if len(s) < 4 else s[:4] if s[2] in v else s[:3]

print(nickname('Michelle'))