n = input()
cnt = 0
str_n = len(n) < 2 and "0"+n or str(n)

while True:
    cnt = cnt + 1
    tmp_n = int(str_n[0]) + int(str_n[1])
    new_n = str_n[1] + str(tmp_n)[-1]
    if int(n) == int(new_n):
        print(cnt)
        break
    else:
        str_n = new_n
