import sys


def vps(s):
    while s.find("()") != -1:
        s = s.replace("()", "")
    if s.strip() == "":
        print("YES")
    else:
        print("NO")


for i in range(int(sys.stdin.readline())):
    st = sys.stdin.readline()
    vps(st)
