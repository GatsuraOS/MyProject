n = int(input("Введите n "))

list_a: list = [1]
print(list_a)

if n != 0:
    for i in range(n+1):
        list_b: list = list_a.copy()
        list_a.append(1)
        # print(list_a)
        # print(list_b)
        for j in range(i):
            list_a[j + 1] = list_b[j] + list_b[j + 1]
        print(list_a)
