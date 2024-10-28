def count_uppar(string):
    uppar =0
    lower =0
    special =0

    for x in string:
        if 'A' <= x <= 'Z':
            uppar +=1
        elif 'a' <= x <= 'z':
            lower += 1
        else:
            special += 1
    return uppar,lower,special

string="Hello WORLD!"
ans =count_uppar(string)
print(ans)
