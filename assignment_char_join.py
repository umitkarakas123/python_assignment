def character(text, n):
    text1 = list(text)
    text1.pop(n)
    final_word = "".join(text1)
    return final_word
print(character("horsepower", 3))

def missing_char(word, n):
    if len(word) >= n :
        word1 = list(word)
        word1.pop(n)
        final_word = ''.join(word1)
        return final_word
    else :
        return("enter correct number!")