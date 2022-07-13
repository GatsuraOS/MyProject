import math


n = int(input("N: "))


with open ("input.txt", "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file]


if len(lines) < n:
    lines *= math.ceil(n // len(lines))


for i in range(n):
    with open(f"output{i + 1}.txt", "w", encoding="utf-8") as file:
        file.write(lines[i])

