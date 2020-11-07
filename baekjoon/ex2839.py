n, r = int(input()), []
for i in range((n // 3) + 1):
    t = (n - i * 3)
    if t % 5 == 0:
        r.append(i + (t // 5))
print(len(r) and min(r) or -1)
