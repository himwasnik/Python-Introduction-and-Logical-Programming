def divisible(nums):
    binarylist = nums.split(',')
    divisible_nums =[]
    for x in binarylist:
        decimal = int(x,2)
        if decimal % 5 == 0:
            divisible_nums.append(x)
    return ",".join(divisible_nums)
    

nums = "0100,0011,1010,1001"
ans = divisible(nums)
print(ans)