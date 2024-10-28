def factorial(num):
    if num == 0 | num ==1:
        return 1
    else:
        return num*factorial(num-1)

num=int(input("enter the number: "))
result = factorial(num)
print(result)
    
