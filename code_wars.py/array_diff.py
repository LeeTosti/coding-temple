def array_diff(a, b):
    if len(b) > 0:
        result = [val for val in a if val not in b]
        return result
    else:
        return a

print(array_diff([1,2,2,2,3],[2]))
print(array_diff([1,2,3], [1, 2]))