t1, t2 = input().split()

tr1 = len(t1)
tr2 = len(t2)

t = []
tr = 0

if tr1 > tr2:
    t2 = "0"*(tr1-tr2) + t2
    tr = tr1
elif tr1 < tr2:
    t1 = "0"*(tr2-tr1) + t1
    tr = tr2
else:
    tr = tr1


up = 0

for i in reversed(range(tr)):
    tmp = int(t1[i]) + int(t2[i]) + up
    if tmp >= 10:
        up = 1
        tmp -= 10
    else:
        up = 0
    t.append(str(tmp))
if up == 1:
    t.append('1')

t.reverse()
print(''.join(t))