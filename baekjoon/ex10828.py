import sys


def solve(o, q=''):
    global r

    if o == 'push':
        r.append(q)
    elif o == 'pop':
        print(len(r) > 0 and r.pop() or -1)
    elif o == 'size':
        print(len(r))
    elif o == 'empty':
        print(len(r) == 0 and 1 or 0)
    elif o == 'top':
        print(len(r) > 0 and r[-1] or -1)


r = []
n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline().split()
    if len(s) > 1:
        solve(s[0], s[1])
    else:
        solve(s[0])
