a, b, c = [int(input()) for i in range(3)]
str_tot = str(a * b * c)
arr = [0] * 10
for i in range(len(str_tot)):
    tmp = int(str_tot[i])
    arr[tmp] = arr[tmp] + 1
for j in range(len(arr)):
    print(arr[j])