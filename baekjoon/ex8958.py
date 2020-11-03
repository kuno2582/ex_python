# My
n = int(input())
for i in range(n):
    txt = input()
    n_scr = 0
    sum_scr = 0
    for j in range(len(txt)):
        if txt[j] == 'O':
            n_scr = n_scr + 1
            sum_scr = sum_scr + n_scr
        else:
            n_scr = 0
    print(sum_scr)

# Short
for i in range(int(input())):
    print(sum([sum(range(len(x)+1)) for x in input().split('X') if x != '']))
