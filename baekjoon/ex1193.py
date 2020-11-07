n, s, i = int(input()), 0, 1
s = n
while s - i > 0:
    s -= i
    i += 1
if i % 2 == 0:
    print(str(s) + '/' + str(i-s+1))
else:
    print(str(i-s+1) + '/' + str(s))

