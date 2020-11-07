# 3 : n, 4n+1, 10n+5, 20n+15, 35n+35
# 2 : n, 3n+1, 6n+4, 10n+10, 15n+20
# 1 : n, 2n+1, 3n+3, 4n+6, 5n+10
# 0 : n, n+1, n+2, n+3, n+4
#


def cal_n(i, j):
    s = 0
    for _ in range(i):
        print('_ : ' + str(_))
        for z in range(1, j + 1):
            o = (_)*z
            print('z : ' + str(o))
            s += o
    return s


#for i in range(int(input())):
x = int(input())
y = int(input())
print(cal_n(x, y))
