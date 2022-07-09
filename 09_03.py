
N = int(input("N "))

def building_matrix(n):
    matrix2 = []
    for i in range(n):
        matrix: list = []
        for j in range(n):
            if i + j == n - 1:
                matrix.append(3)
            elif i + j == n - 2:
                matrix.append(2)
            else:
                matrix.append(1)
        matrix2.append(matrix)
    return matrix2


my_matrix = building_matrix(N)
for i in range(N):
    print(my_matrix[i])

