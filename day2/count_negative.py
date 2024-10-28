def countnegative(num):
    negative = []
    for x in num:
        if x < 0:
            negative.append(x)
    return len(negative)

num = [-1, 2, -3, 4, -5, 6, -7]
ans = countnegative(num)
print(ans)
