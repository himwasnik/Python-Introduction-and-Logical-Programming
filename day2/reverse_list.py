def reverselist(num):
    left = 0 
    right = len(num) - 1 

    while left < right:
        num[left], num[right] = num[right], num[left]
        left += 1
        right -= 1
    return num

num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ans = reverselist(num)
print(ans)
