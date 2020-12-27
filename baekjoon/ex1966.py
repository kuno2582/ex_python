# My
from collections import deque

for t in range(int(input())):
    n, m = map(int, input().split())
    r = list(map(int, input().split()))
    j = deque()
    cnt = 0
    for i in range(len(r)):
        if i == m:
            j.append({"number": r[i], "p": "o"})
        else:
            j.append({"number": r[i], "p": "x"})
    flg = True
    while flg:
        this_number = j[0]["number"]
        this_point = j[0]["p"]

        f_flg = False
        for k in j:
            if k['number'] > this_number:
                j.append(j.popleft())
                f_flg = True
                break
        if f_flg:
            continue

        this_number = j[0]["number"]
        this_point = j[0]["p"]

        cnt += 1

        if this_point == 'o':
            flg = False
            break
        else:
            j.popleft()

    print(cnt)


# Short
"""
Q = int(input())
for i in range(Q):
	N, index = map(int,input().split())
	queue = list(map(int,input().split()))
	count=0
	while True:
		if max(queue) == queue[0]:
			queue.pop(0)
			count+=1
			if index==0:print(count);break
			else:index-=1
		else:
			tmp = queue.pop(0)
			queue.append(tmp)
			if index==0:index=len(queue)-1
			else:index-=1
"""