import sys
import heapq as hq
n = int(sys.stdin.readline())
heap = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap):
            print(hq.heappop(heap)[1])
        else:
            print(0)
    else:
        hq.heappush(heap, (-x, x))
