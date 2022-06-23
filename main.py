text: str = input("Введите текст: ")
dictinary = {i: text.count(i) for i in text}

print(dictinary)