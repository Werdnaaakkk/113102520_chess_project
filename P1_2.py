# P1_2
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

if checkerboard[x2][y2] == 1:
    print('No')
elif (x1 == x2 and y1 == y2) or (abs(x2 - x1) != abs(y2 - y1) and x1 != x2 and y1 != y2):
    print('No')

else:
    dx = (x2 - x1) // max(1, abs(x2 - x1))
    dy = (y2 - y1) // max(1, abs(y2 - y1))

    cx, cy = x1 + dx, y1 + dy
    reachable = True

    while (cx, cy) != (x2, y2):
        if checkerboard[cx][cy] == 1:
            reachable = False
            break
        cx += dx
        cy += dy

    if reachable:
        print('Yes')
    else:
        print('No')
