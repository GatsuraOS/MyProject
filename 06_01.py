numb = int(input("введите число "))


def des2bin(n: int) -> str:
    return bin(n)


binar = list(des2bin(numb))
binar = "".join(binar[2:])
print(binar)


def bin2des(n: str) -> int:
    des = 0
    l = len(n)

    for i in range(l):
        if n[i] == "1":
            des += 2 ** (l - 1 - i)

    return des


print(bin2des(binar))
