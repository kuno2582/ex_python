a, b = map(int, input().split())


def cal_time(h, m, diff_m):
    result_m = m + diff_m
    while result_m < 0:
        h = h - 1
        result_m = 60 + result_m
    while result_m > 59:
        h = h + 1
        result_m = result_m - 60
    while h < 0:
        h = 24 + h
    while h > 23:
        h = h - 24

    print(h, result_m)


cal_time(a, b, -45)
