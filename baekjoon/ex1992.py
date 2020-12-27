# n = 8
# str = """11110000
# 11110000
# 00011100
# 00011100
# 11110000
# 11110000
# 11110011
# 11110011"""
# r = [list(x) for x in list(str.split('\n'))]
n, r = int(input()), []
for i in range(n):
    r.append(input())


def quad_tree(ar):
    s = sum([sum(list(map(int, x))) for x in ar])
    l = len(ar)
    if s == 0:
        return '0'
    elif s == l * l:
        return '1'
    else:
        return '(' + quad_tree(list(x[:int(len(ar) / 2)] for x in ar[:int(len(ar) / 2)])) + quad_tree(
            list(x[int(len(ar) / 2):] for x in ar[:int(len(ar) / 2)])) + quad_tree(
            list(x[:int(len(ar) / 2)] for x in ar[int(len(ar) / 2):])) + quad_tree(
            list(x[int(len(ar) / 2):] for x in ar[int(len(ar) / 2):])) + ')'


q = quad_tree(r)
print(q)
