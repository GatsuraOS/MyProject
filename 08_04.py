my_numbers: list = [2, 3, 11, 18, -5, -12, 0, 2, 7]
action: bool = True

while action:
    action = False
    for i in range(len(my_numbers) - 1):
        if my_numbers[i] > my_numbers[i + 1]:
            a = my_numbers[i]
            my_numbers[i] = my_numbers[i + 1]
            my_numbers[i + 1] = a
            action = True

print(my_numbers)