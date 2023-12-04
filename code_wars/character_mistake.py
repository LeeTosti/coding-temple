def correct(s):
    replacements = {'0':'O', '5':'S', '1':'I'}
    for k, v in replacements.items():
        s = s.replace(k, v)
    return s

print(correct('L0ND0N'))