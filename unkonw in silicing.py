sumt = 0
number = input("number:")
for x in number[::2]:
    sumt = int(x) + sumt
    print(sumt)