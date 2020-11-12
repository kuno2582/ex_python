n, r = int(input()), []
for i in range(n):
    r.append(int(input()))
r.sort()
for x in range(n):
    print(r[x])
