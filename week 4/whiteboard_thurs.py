#Given an integer n, return the largest number that contains exactly n digits.

#Example

#For n = 2, the output should be
#solution(n) = 99.

def sol(n):
    return int(n*'9')

print(sol(10))
