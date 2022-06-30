lst = [1, 3, "hello", 5.67, True, " world"]


def filter_str(my_list):
    for i in range(len(my_list)):
        if isinstance(my_list[i], str):
            return True
        else:
            return False


lst = list(filter(filter_str, lst))
print(lst)