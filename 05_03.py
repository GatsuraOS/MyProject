N = int(input("Введите N "))

for i in range(1, N + 1):
         if i % 5:
             if not i % 2:
                 print(i, end = ", ")
         elif not i % 5:
              if not i % 2:
                 print(i)