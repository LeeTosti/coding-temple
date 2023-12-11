#def persistence(n):
#    count = 0
#    if len(n) <=1:
#        return count
#    while len(n) > 1:
#        result = 1
#        for x in n:
#            result = result * x
#
#def persistence(n):
#    n = str(n)
#    count = 0
#    while len(n) > 1:
#        p = 1
#        for i in n:
#            p *= int(i)
#        n = str(p)
#        count += 1
#    return count



#
#
def persistence(n, count = 0):
    if len(str(n)) == 1:
        return count
    arr_n = [int(i) for i in str(n)]
    product = 1
    for i in range(len(arr_n)):
        product *= arr_n[i]
    count = persistence(product, count)
    count += 1
    return count

print(persistence(25))