def reverse_string(sentence):
    words = sentence.split(" ")
    reversed_words = []
    
    for word in words:
        reversed_word = ""
        for char in word:
            reversed_word = char + reversed_word 
        reversed_words.append(reversed_word)
    
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

sentence = "i am a student"
ans = reverse_string(sentence)
print(ans)  
