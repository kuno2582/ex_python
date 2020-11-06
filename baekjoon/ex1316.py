# My
def cnt(t):
    q, r, c = t[0], [], 0
    for i in range(len(t)):
        if t[i] == q:
            c += 1
        else:
            r.append(c)
            c = 1
            q = t[i]
    return len(r)


a = 0
for j in range(int(input())):
    s = input()
    if cnt(s) == cnt(sorted(s)):
        a += 1
print(a)

# Short
n = 0
for i in range(int(input())):
    w = input()
    n += list(w) == sorted(w, key=w.find)
print(n)
