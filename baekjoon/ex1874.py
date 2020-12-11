import sys

n, s, op = int(sys.stdin.readline()), [], []
cnt = 1
t = True
for i in range(int(n)):
    num = int(sys.stdin.readline())
    while cnt <= num:
        s.append(cnt)
        op.append('+')
        cnt += 1
    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        t = False
if t:
    for i in op:
        print(i)
else:
    print('NO')
