# My
s = input().upper()
cnt_arr = [0] * 32
for i in range(len(s)):
    tmp = ord(s[i])-65
    cnt_arr[tmp] = cnt_arr[tmp] + 1

max_arr = []
max_num = 0
for i in range(len(cnt_arr)):
    if cnt_arr[i] > max_num:
        max_num = cnt_arr[i]
        max_arr = [i]
    elif cnt_arr[i] == max_num:
        max_arr.append(i)

if len(max_arr) > 1:
    print('?')
else:
    print(chr(max_arr[0]+65))


# Short
s = input().upper()
m = 0
for i in set(s):
    c = s.count(i)
    if m == c:
        o = '?'
    if m < c:
        m = c
        o = i
print(o)
