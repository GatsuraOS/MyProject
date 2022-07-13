import itertools


n = int(input("N: "))
amount_of_files = 3

with open("input.txt", "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file]

print(lines)

for i in range(0, len(lines), n):
    with open(f"output{i/n+1}.txt", "w", encoding="utf-8") as file:
        for j in range(n):
            if i + j < len(lines):
                file.write(lines[i+j] + "\n")
