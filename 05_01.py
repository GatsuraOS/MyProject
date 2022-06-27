N = int(input("введите количество цифр "))
M = int(input("введите число, которому кратно "))
K = int(input("введите число, больше которого "))

for i in range(K + 1, N * M + K):
    if i > K and not i % M:
        print(i)