def divisibal():
    num =[]
    for i in range(2000,3500):
        if i % 7 ==0 and i % 5 ==0:
            num.append(i)
    return num

ans= divisibal()
print(ans)