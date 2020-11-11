n, r = int(input()), []
for i in range(n):
    s = sum([int(x) for x in str(i)]) + i
    if s == n:
        r.append(i)
if len(r) == 0:
    print(0)
else:
    print(min(r))
