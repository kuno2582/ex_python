a, b = map(int, [x[::-1] for x in input().split()])
print(a > b and a or b)