# import sys
import os
#import readchar

list_a = ["hello", "world", "!!!"]
i = 0
simb = "s"
print(list_a[i])
while simb != "`":
    #simb = readchar.readchar()
    simb = input()
    if simb == ">":
        i += 1
        if i == len(list_a):
            i = 0
    elif simb == "<":
        i -= 1
        if i < 0:
            i = len(list_a) - 1
    # else:
    #     if simb == "`":
    #         break
    os.system('cls')
    print(list_a[i])