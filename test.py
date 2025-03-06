ls = [[12, 2], [10]]

for l in ls:
    print(l[0])
    try:
        print(l[1])
    except IndexError:
        pass