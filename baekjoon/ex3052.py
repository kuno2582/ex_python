# My
arr = [int(input()) for i in range(10)]
arr2 = []
for i in range(len(arr)):
    tmp = arr[i] % 42
    if tmp not in arr2:
        arr2.append(tmp)
print(len(arr2))

# Short
print(len({int(input()) % 42 for i in range(10)}))
