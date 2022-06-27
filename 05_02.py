numb1 = float(input("введите число 1 "))
action = input("введите действие ")
numb2 = float(input("введите число 2 "))

if action == "+":
    print(numb1 + numb2)
elif action == "-":
    print(numb1 - numb2)
elif action == "*":
    print(numb1 * numb2)
elif action == "/":
    print(numb1 / numb2)
else: print("действие не распознано")