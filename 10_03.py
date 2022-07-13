with (
    open("input.txt", "r", encoding="utf-8") as file,
    open("output.txt", "w", encoding="utf-8") as file2
):
    for line in file:
        lines = line.split()
        file2.write(str(len(lines)) + "\n")

