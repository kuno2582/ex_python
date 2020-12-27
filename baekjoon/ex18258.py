from collections import deque
import sys

r = deque()
for i in range(int(sys.stdin.readline())):
    o = sys.stdin.readline().split()
    if o[0] == 'push':
        r.append(o[1])
    elif o[0] == 'pop':
        if len(r):
            print(r[0])
            r.popleft()
        else:
            print(-1)
    elif o[0] == 'size':
        print(len(r))
    elif o[0] == 'empty':
        if len(r):
            print(0)
        else:
            print(1)
    elif o[0] == 'front':
        if len(r):
            print(r[0])
        else:
            print(-1)
    elif o[0] == 'back':
        if len(r):
            print(r[-1])
        else:
            print(-1)