numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers2 = []
N = int(input("введите N "))

for i in range(len(numbers), 0, -1):
    if -i < -N:
        numbers2.append(numbers[-i])
    else:
        numbers2.insert(0, numbers[-i])

print(numbers2)