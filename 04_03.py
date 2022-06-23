N = int(input("N="))
my_lst = [i for i in range(1, N + 1)]
dictinary = dict.fromkeys(my_lst, [{"name": input("name "), "email": input("email ")}])

print(dictinary)
