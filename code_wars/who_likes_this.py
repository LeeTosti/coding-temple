def likes(names):
    name_count = len(names)
    if name_count == 0:
        return f'no one likes this'
    elif name_count == 1:
        return f'{names[0]} likes this'
    elif name_count == 2:
        return f'{names[0]} and {names[1]} like this'
    elif name_count == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif name_count > 3:
        return f'{names[0]}, {names[1]} and {name_count - 2} others like this'

print(likes([]))
print(likes(["Peter"]))
print(likes(["Jacob", "Alex"]))
print(likes(["Max", "John", "Mark"]))
print(likes(["Alex", "Jacob", "Mark", "Max"]))