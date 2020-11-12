def print_arr(ar):
    a, b = 0, 0
    for i in range(len(ar)):
        for j in range(len(ar[i])):
            if (i+j) % 2 == 0:
                if ar[j][i] == 'W':
                    a += 1
                else:
                    b += 1
            else:
                if ar[j][i] == 'B':
                    a += 1
                else:
                    b += 1
    return min(a, b)


n, m = map(int, input().split())
s = []
for q in range(n):
    s.append(input())

r, o = [list(c) for c in s], []
for x in range(len(r)-7):
    tmp = r[:][x:x+8]
    for y in range(len(r[x])-7):
        tmp2 = [k[y:y+8] for k in tmp]
        o.append(print_arr(tmp2))
print(min(o))
