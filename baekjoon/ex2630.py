# str = """1 1 0 0 0 0 1 1
# 1 1 0 0 0 0 1 1
# 0 0 0 0 1 1 0 0
# 0 0 0 0 1 1 0 0
# 1 0 0 0 1 1 1 1
# 0 1 0 0 1 1 1 1
# 0 0 1 1 1 1 1 1
# 0 0 1 1 1 1 1 1"""
# ar = []
# for x in str.split('\n'):
#     ar.append(list(map(int, x.split())))
ar = []
for i in range(int(input())):
    ar.append(list(map(int, input().split())))

cnt_blue = 0
cnt_white = 0


def chkRec(r):

    global cnt_blue, cnt_white

    len_r = len(r)
    sum_r = sum(list(sum(x) for x in r))
    len_sub = int(len(r)/2)

    if len_r * len_r == sum_r:
        cnt_blue += 1
    elif sum_r == 0:
        cnt_white += 1
    else:
        r1 = [x[:len_sub] for x in r[:len_sub]]
        r2 = [x[len_sub:] for x in r[:len_sub]]
        r3 = [x[:len_sub] for x in r[len_sub:]]
        r4 = [x[len_sub:] for x in r[len_sub:]]
        chkRec(r1)
        chkRec(r2)
        chkRec(r3)
        chkRec(r4)


chkRec(ar)
print(cnt_white)
print(cnt_blue)
