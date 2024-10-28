def counting(words):
    dictionary = {}
    for x in words:
        if x in dictionary:
            dictionary[x] +=1
        else:
            dictionary[x] =1
    return dictionary


words = ["apple", "banana", "apple", "orange", "banana", "apple"]
ans = counting(words)
print(ans)