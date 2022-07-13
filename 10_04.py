with (
    open("input.txt", "r", encoding="utf-8") as file,
    open("output.txt", "w", encoding="utf-8") as file2
):
    for line in file:
        line = line.strip()
        line = list(reversed(line))
        file2.write("".join(line) + "\n")
