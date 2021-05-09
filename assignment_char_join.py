def character(text, i):
    text1 = list(text)
    text2 = text1.pop(i)
    final_word = "".join(text1)
    return final_word
print(character("horsepower",3))