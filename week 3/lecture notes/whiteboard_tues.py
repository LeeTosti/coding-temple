#Complete the square sum function so that it squares each number passed into it and then sums the results together.
#For example, for [1, 2, 2] it should return 9 because 1^2+2^2+2^2=9.

def sol(numbers):
    sum_of_squares = 0
    for num in numbers:
        sum_of_squares += num**2
    return sum_of_squares

print(sol([4,1,2,2]))

def sol(numbers):
    #return sum(num**2 for num in numbers)
    return sum([num**2 for num in numbers])
print(sol([4,1,2,2]))