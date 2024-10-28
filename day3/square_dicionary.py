def squaretill(num):
    count_dic={}
    for i in range(1,num+1):
        count_dic[i] = i*i
    return count_dic

num = int(input("Enter the number"))
ans = squaretill(num)
print(ans)