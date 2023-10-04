#You get an array of numbers, return the sum of all of the positives ones.

#Example [1,-4,7,12] => 1 + 7 + 12 = 20

#Note: if there is nothing to sum, the sum is default to 0.

def sol(numbers):
    sum_of_pos = 0
    for number in numbers:
        if number == abs(number):
            sum_of_pos += number
    return sum_of_pos

output = sol([1, -4, 7, 12])
print(output)

def sol(numbers):
    return sum([x for x in numbers if x == abs(x)])

output = sol([1, -4, 7, 12])
print(output)