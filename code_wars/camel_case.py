#def to_camel_case(text):
#    import re
#    text = re.split('-|_', text)
#    for i in range(len(text)):
#        if text[i] == text[i].lower():
#            text[i] == text[i].title()
#    text = ''.join(text)
#    return text

def to_camel_case(text):
    import re
    text = re.split('-|_', text)
    new_text = []
    for t in text:
        new_text.append(t.title())
    new_text = ''.join(new_text)
    return new_text

#print(to_camel_case("The_Stealth-Warrior"))
print(to_camel_case("the-stealth-warrior"))
#print(to_camel_case("The_Stealth_Warrior"))