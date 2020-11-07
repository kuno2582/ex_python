# My
def cal(r):
    r_len = len(r)
    if r_len == 1:
        return True
    else:
        arr = []
        for n in range(1, r_len):
            arr.append(int(r[n]) - int(r[n - 1]))
        if len(set(arr)) == 1:
            return True
        else:
            return False


cnt = 0
for i in range(1, int(input()) + 1):
    if cal(str(i)):
        cnt = cnt + 1
print(cnt)

# Short
