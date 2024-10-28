def lowertouppar(string):
    result=""
    for i in string:
        if i.islower():
            result +=i.upper()
        else:
            result += i
    return result
string= 'Hello world Practice makes perfect'
ans = lowertouppar(string)
print(ans)
