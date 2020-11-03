nMax, nSeq = 0, 0
for i in range(0, 9):
    tmp = int(input())
    if tmp > nMax:
        nMax = tmp
        nSeq = i + 1

print(nMax)
print(nSeq)
