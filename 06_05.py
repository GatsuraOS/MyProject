my_list = [1, 2, 3, 4, 5, 6]
j = len(my_list)

for i in range(len(my_list) // 2):
    swap = my_list[i]
    my_list[i] = my_list[j - 1]
    my_list[j - 1] = swap
    j -= 1

print(my_list)