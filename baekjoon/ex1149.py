import copy

r_n = [0, 0, 0]
for i in range(int(input())):
    r_p = copy.deepcopy(r_n)
    r_t, r_n = list(map(int, input().split())), []
    for j in range(3):
        n_a = min([val+r_t[j] for idx, val in enumerate(r_p) if idx != j])
        r_n.append(n_a)
print(min(r_n))
