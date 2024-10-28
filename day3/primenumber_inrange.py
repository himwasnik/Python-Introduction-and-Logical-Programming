def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primenumber():
    number = []
    for x in range(2000, 3000):
        if is_prime(x):
            number.append(x)
    return number

ans =primenumber()
print(ans)