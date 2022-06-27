text = input("Введите текст: ")
key = input("Введите ключ: ")


def str2bin(text: str, encoding="cp1251") -> str:
    return " ".join(
        bin(c)[2:].rjust(8, "0") for c in text.encode(encoding)
    )
text = list(str2bin(text))
print(" ".join(text))
key = list(str2bin(key))
print(" ".join(key))


for i in range(len(text)):
    if text[i] == key[i] and text[i] != " ":
        text[i] = "0"
    elif text[i] != key[i]:
         text[i] = "1"

print(" ".join(text))