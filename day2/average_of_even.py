def average_of_even(num):
    #list comprihention
    even_number=[x for x in num if x % 2 == 0]
    avg = sum(even_number)/len(even_number)
    return avg

num=[1,2,3,4,5,6,7,8,9,12]
ans = average_of_even(num)
print(ans)
