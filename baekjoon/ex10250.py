for i in range(int(input())):
    h, w, n = map(int, input().split())
    if (n % h) == 0:
        x, y = ((n-1) // h) + 1, h
    else:
        x, y = (n // h) + 1, (n % h)
    print(str(y) + (len(str(x)) < 2 and '0'+str(x) or str(x)))
