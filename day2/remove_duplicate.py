def duplictae(num):
    blank =[]
    for x in num:
        if x not in blank:
            blank.append(x)
    return blank

num = [5,1,24,89,3,2,4,87,6,2,214,89]
ans = duplictae(num)
print(ans)