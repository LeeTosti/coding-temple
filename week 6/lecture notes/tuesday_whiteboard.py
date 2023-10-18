# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
    s = ''
    new_text = text.split(' ')
    for i in new_text:
        s += i[::-1]
        s += ' '
    s = s.strip()
    return s

print(reverse_words("This is an example!"))