for i in range(int(input())):
    print(sum([sum(range(len(x)+1)) for x in input().split('X') if x != '']))
