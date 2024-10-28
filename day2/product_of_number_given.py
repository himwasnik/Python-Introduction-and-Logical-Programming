def productnumber(num,divisor):
    divisibale = [x for x in num if x % divisor == 0]
    product = 1
    for x in divisibale:
        product *= x
    return product
    

num= [1, 2, 3, 4, 5, 6, 7, 8, 9]
divisor = 2
ans = productnumber(num,divisor)
print(ans)

