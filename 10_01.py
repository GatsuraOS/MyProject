n = int(input("N: "))


with open ("input.txt", "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file]


for i in range(n):
    with open(f"output{i + 1}.txt", "w", encoding="utf-8") as file:
        if i >= len(lines):
            file.write(lines[i - len(lines)])
        else:
            file.write(lines[i])

