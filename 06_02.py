morze = {
    "A": ".-", "0": "-----",
    "B": "-...", "1": ".----",
    "C": "-.-.", "2": "..---",
    "D": "-..", "3": "...--",
    "E": ".", "4": "....-",
    "F": "..-.", "5": ".....",
    "G": "--.", "6": "-....",
    "H": "....", "7": "--...",
    "I": "..", "8": "---..",
    "J": ".---", "9": "----.",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
}

text = input("введите текст: ")
text = text.upper()


# def decorator(upper):
#    def registr(**kwargs):
#        result = upper(**kwargs)
#        print(result)
#        return result
#    return registr


# @decorator
def tr_morze(text: str) -> str:
    for i in text:
        if i != " ":
            simb = morze[i]
        else:
            simb = ""
        print(simb, end=" ")


print(tr_morze(text))