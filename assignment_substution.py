def front_back(word):
    if len(word) == 1:
        return word
    elif len(word) > 1 :
        c = list(word)
        c.pop(0)
        c.pop(-1)
        c.insert(0, word[-1])
        c.insert(len(c), word[0])
        end1 = "".join(map(str, c))
        return end1
print(front_back('HELLO'))