import re


def vps(s):
    while s.find("()") != -1 or s.find("[]") != -1:
        s = s.replace("()", "")
        s = s.replace("[]", "")
    if s.strip() == "":
        print("yes")
    else:
        print("no")


while True:
    st = input()
    if st == '.':
        break
    else:
        st = re.sub('[^\[\(\)\]]', '', st)
        vps(st)
