def alphabet_position(text):
    alpha = '#abcdefghijklmnopqrstuvwxyz'
    alpha_dict = {}
    for i in range(27):
        alpha_dict[alpha[i]] = i
    new_text = []
    for key in text.lower():
        if key in alpha_dict:
            new_text.append(str(alpha_dict[key]))
    return ' '.join(new_text)



print(alphabet_position("The sunset sets at twelve o' clock."))

