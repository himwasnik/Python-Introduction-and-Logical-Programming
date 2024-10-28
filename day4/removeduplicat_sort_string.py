def stringduplicate(words):
    unique = set(words.split(" "))
    sortedword =sorted(unique)
    return " ".join(sortedword) 


words="hello world and practice makes perfect and hello world again"
ans= stringduplicate(words)
print(ans)