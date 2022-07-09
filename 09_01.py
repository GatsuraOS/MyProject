my_list = ["hello", "world", 1, 2, 3, 4, 4, 3, 2, 1, "world", "hello"]
simmetric_list = []

def simmetric(my_list, simmetric_list):
    for i in range((len(my_list)//2)):
        if my_list[i] == my_list[-1 - i]:
            simmetric_list.append(True)
        else:
            simmetric_list.append(False)
    return simmetric_list



if simmetric(my_list, simmetric_list).count(False) == 0:
    print("Your list is simmetric")
else:
    print("Your list is not simmetric")