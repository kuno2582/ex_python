# My
n = int(input())
arr = list(map(int, input().split()))
nMax = max(arr)
n_arr = [x / nMax * 100 for x in arr]
print(sum(n_arr) / n)

# Short
n = int(input())
arr = list(map(int, input().split()))
print(sum(arr) / max(arr) / n * 100)
