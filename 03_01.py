text = input("Введите текст: ")

# способ 1
print("-".join(text.split()))

#способ 2
print(text.replace(" ","-"))