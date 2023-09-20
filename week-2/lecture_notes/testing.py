key_1 = ['Name', 'Age', 'Hair Color', 'Eye Color']
key_2 = ['City', 'State', 'Country']
val_1 = ['Lee', 38, 'Brown', 'Brown']
val_2 = ['Chicago', 'IL', 'Country']



dict_1 = dict(zip(key_1, val_1))
dict_2 = dict(zip(key_2, val_2))
dict_3 = (dict_1, dict_2)

print(dict_3)

##def merge():
 #   dict_1 = {}
 #   for key, value in key_1, val_1:
 #       return dict_1.append([key, value])
#
 #   tuple_1 = [(key, value) for i, (key, value) in enumerate(zip(key_1, val_1))]
 #   tuple_2 = [(key, value) for i, (key, value) in enumerate(zip(key_1, val_1))]
 #   dict_1 = dict(tuple_1)
 #   dict_2 = dict(tuple_2)
 #   return dict(dict_1 + dict_2)