for k in range(int(input())):
    n = int(input())
    a, b, c = 1, 1, 1
    for i in range(n-3):
        a, b, c = b + c, a, b
    print(a)
