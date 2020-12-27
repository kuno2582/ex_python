import sys
while True:
    x, y = map(int, sys.stdin.readline().split())
    if x == 0 and y == 0:
        break
    else:
        if x % y == 0:
            print('multiple')
        elif y % x == 0:
            print('factor')
        else:
            print('neither')
