a: str = input("Введите строку А ")
b: str = input("Введите строку B ")


def char_comparer(text1, text2):
    counter = 0
    for i in range(len(text1)):
        if text1[i] == text2[i]:
            counter += 1
    return(counter)

if a < b:
    print(char_comparer(a, b))
else:
    print(char_comparer(b, a))
