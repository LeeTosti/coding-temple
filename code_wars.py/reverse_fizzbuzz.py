def reverse_fizz_buzz(array):
    fizz_val = 0
    buzz_val = 0
    fizzbuzz_val = 0
    for i, val in enumerate(array):
        if val == 'FizzBuzz':
            fizzbuzz_val += i+1
            break
    for i, val in enumerate(array):
        if val == 'Fizz':
            fizz_val += i+1
            break
    for i, val in enumerate(array):    
        if val == 'Buzz':
            buzz_val += i+1
            break
    if buzz_val > 0 and fizz_val > 0:
        return (fizz_val, buzz_val)
    if fizz_val == 0 and buzz_val == 0:
        return (fizzbuzz_val, fizzbuzz_val)
    if buzz_val == 0:
        return (fizz_val, fizzbuzz_val)
    if fizz_val == 0:
        return (fizzbuzz_val, buzz_val)
    
#def reverse_fizz_buzz(array):
    #fizz = array.index("Fizz") if "Fizz" in array else array.index("FizzBuzz")
    #buzz = array.index("Buzz") if "Buzz" in array else array.index("FizzBuzz")
    #return (fizz+1, buzz+1)

print(reverse_fizz_buzz([1,'Fizzbuzz', 3, 'Fizzbuzz', 5, 'FizzBuzz']))