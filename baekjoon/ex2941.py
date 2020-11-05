a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
for x in range(len(a)):
    s = s.replace(a[x], str(x))
print(len(s))
