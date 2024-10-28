def oddavg(num):
    count =0
    sum=0
    for x in num :
        if x % 2 != 0:
            sum += x
            count +=1
            result = sum / count
    return result
    
num=[1,2,3,4,5,6,7,8,9]
ans=oddavg(num)
print(ans)



