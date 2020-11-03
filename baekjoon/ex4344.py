# My
for i in range(int(input())):
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    avg = round(sum(arr) / n, 3)
    n_arr = [x for x in arr if x > avg]
    print('%.3f%%' % round((len(n_arr) / n * 100), 3))
