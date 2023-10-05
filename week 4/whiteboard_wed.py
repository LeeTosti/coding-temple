# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.

# Don't forget the space after the closing parentheses!

def sol(a):
    return f'({a[0:3]}) {a[3:6]}-{a[6:]}'

phone_number = sol([5,1,8,7,2,7,3,0,0,6])
print(phone_number)