# P1_1
position1 = input().split()
position2 = input().split()

x1, y1 = int(position1[0]), int(position1[1])
x2, y2 = int(position2[0]), int(position2[1])

if not (0 <= x2 <= 7 and 0 <= y2 <= 7):
    print('No')
elif x1 == x2 and y1 == y2:
    print('No')
elif checkerboard[x2][y2] == 1:
    print('No')
else:
    if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
        print('Yes')
    else:
        print('No')
