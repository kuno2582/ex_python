r = [((ord(x) - (ord(x) >= 83 and 66 or 65)) // 3)+2 for x in input().replace('Z', 'Y')]
print(sum(r)+len(r))
