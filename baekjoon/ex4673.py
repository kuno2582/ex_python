# My
def self_gen(n):
    return n + sum(list(int(x) for x in str(n)))


arr = []
for i in range(10000):
    arr.append(i + 1)
for i in range(10000):
    x = self_gen(i + 1)
    if x in arr:
        arr.remove(x)
for i in range(len(arr)):
    print(arr[i])

# Short
r = range(1, 10001)
s = sorted(set(r) - {x + sum(map(int, str(x))) for x in r})
print(*s, sep="\n")
