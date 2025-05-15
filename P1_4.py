# P1_4
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

dx = abs(x2 - x1)
dy = abs(y2 - y1)

if (x1 == x2 and y1 == y2) or checkerboard[x2][y2] == 1:
    print("No")
elif (dx, dy) in [(2, 1), (1, 2)]:
    print("Yes")
else:
    print("No")
