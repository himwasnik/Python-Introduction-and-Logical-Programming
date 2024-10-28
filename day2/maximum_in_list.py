def maxiumelement(num):
    max= num[0]
    for i in range(1,len(num)):
        if num[i] > max:
             max =num[i]
    return max

num = [1,2,4,5,7,89,96,7,412,5,97,55]
ans = maxiumelement(num)
print(ans)