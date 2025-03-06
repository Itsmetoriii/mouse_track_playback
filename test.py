ls = [[12, 2, True], [14, 4], [15, 6, True]]

for coor in ls:
    if True in coor:
        print('Boom')
    else:
        print('Toom')