chislo1 = input("Введите число 1: ")
chislo2 = input("Введите число 2: ")
chislo3 = input("Введите число 3: ")
chislo1 = float(chislo1.replace(",", "."))
chislo2 = float(chislo2.replace(",", "."))
chislo3 = float(chislo3.replace(",", "."))


pozitive = (str(chislo1 > 0) + str(chislo2 > 0) + str(chislo3 > 0)).count("True")
negotive = (str(chislo1 > 0) + str(chislo2 > 0) + str(chislo3 > 0)).count("False")
print(f"В введенных вами числах {pozitive} больше нуля и {negotive} меньше нуля.")