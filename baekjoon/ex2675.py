n = int(input())
for i in range(n):
    r, s = input().split()
    print(''.join([x * int(r) for x in s]))
