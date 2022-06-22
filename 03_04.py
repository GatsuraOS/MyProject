chislo1 = input("Введите число 1: ")
chislo2 = input("Введите число 2: ")
chislo3 = input("Введите число 3: ")
chislo1 = float(chislo1.replace(",", "."))
chislo2 = float(chislo2.replace(",", "."))
chislo3 = float(chislo3.replace(",", "."))


pozitive = (chislo1 > 0) + (chislo2 > 0) + (chislo3 > 0)
negotive = (chislo1 < 0) + (chislo2 < 0) + (chislo3 < 0)
print(f"В введенных вами числах {pozitive} больше нуля и {negotive} меньше нуля.")