def cal(i, j, n):
    if ((i // n) % 3 == 1) and ((j // n) % 3 == 1):
        print(' ', end='')
    else:
        if n//3 == 0:
            print('*', end='')
        else:
            cal(i, j, n/3)


n = int(input())
for i in range(n):
    for j in range(n):
        cal(i, j, n)
    print()
