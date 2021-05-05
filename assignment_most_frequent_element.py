numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
frequent = max(set(numbers), key = numbers.count)  # liste içindeki en fazla tekrar eden sayı
item = numbers.count(frequent)  # liste içinde en fazla tekrar eden sayının tekrar sayısı
print(f"the most frequent number is {frequent} and it was {item} times repeated")  # En sık tekrarlana sayı "frequent" tekrarlama sayısı "item"