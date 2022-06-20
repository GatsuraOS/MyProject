chislo1 = input("Введите число 1: ")
chislo2 = input("Введите число 2: ")
chislo3 = input("Введите число 3: ")
chislo1 = float(chislo1.replace(",", "."))
chislo2 = float(chislo2.replace(",", "."))
chislo3 = float(chislo3.replace(",", "."))

print(round(((chislo1 + chislo2 + chislo3)/3), 3))