from itertools import *

n = int(input())
r = list(map(int, input().split()))
o = list(map(int, input().split()))
q, ar = [], []


def cal(x, y, o):
    if o == '+':
        return x + y
    elif o == '-':
        return x - y
    elif o == '*':
        return x * y
    elif o == '/':
        return int(x / y)


for i in range(len(o)):
    if i == 0:
        s = '+'
    elif i == 1:
        s = '-'
    elif i == 2:
        s = '*'
    elif i == 3:
        s = '/'
    q.extend([s] * o[i])

p = permutations(q, len(q))

for i in set(p):

    s = 0
    for j in range(len(i)):
        if j == 0:
            a, b = r[0], r[1]
        else:
            a, b = s, r[j + 1]
        s = cal(a, b, i[j])
    ar.append(s)

print(max(ar))
print(min(ar))
