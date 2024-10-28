def countoccurance(num):
    count_dic={}
    for i in num:
        if i in count_dic:
            count_dic[i] +=1
        else:
            count_dic[i]=1
    return count_dic

num = [1,1,1,1,12,2,2,2,2,2,3,3,3,3,]
ans=countoccurance(num)
for element, count in ans.items():
    print(f"Element {element} occurs {count} times")