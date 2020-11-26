n = int(input())

a, b = 1, 0
for i in range(n):
    a, b = (a + b) % 15746, a % 15746
print(a)