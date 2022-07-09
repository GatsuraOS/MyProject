array = [[1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1],
        [0, -2, 3, 4, 9],
        [-7, -8, 2, 3, -4],
        [0, 2, 4, -6, -8]]


def filtration(my_array: list) -> int:
    sum_numbers: int = 0
    for i in range(len(my_array)):
        for j in range(len(my_array[0])):
            if my_array[i][j] < 0 and my_array[i][j] // 2:
                sum_numbers += abs(my_array[i][j])
    return sum_numbers


print(filtration(array))