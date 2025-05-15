# P1_3
position1 = input().split()
x1, y1 = int(position1[0]), int(position1[1])

position2 = input().split()
x2, y2 = int(position2[0]), int(position2[1])

if x1 == x2 and y1 == y2:
    print('No')
elif checkerboard[x2][y2] == 1:
    print('No')
else:
    if y1 == y2 and x2 - x1 == 1:
        print('Yes')
    else:
        print('No')
