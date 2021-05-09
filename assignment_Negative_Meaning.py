def not_string(text):
    if list(text[:4]) == ["n", "o", "t", " "] or list(text[:4]) == ["N", "o", "t", " "] or list(text[:4]) == ["N", "O", "T", " "] :
        return (text)
    else :
        return (f"not {text}") 
print(not_string("NOT Bad"))
