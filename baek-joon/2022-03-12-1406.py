import sys

l = list(sys.stdin.readline().strip())
r = list()
num = int(sys.stdin.readline())
for i in range(num):
    c = sys.stdin.readline().split()
    if c[0] == "L":
        if len(l) != 0:
            r.append(l.pop())
    elif c[0] == "D":
        if len(r) != 0:
            l.append(r.pop())
    elif c[0] == "B":
        if len(l) != 0:
            l.pop()
    else:
        l.append(c[1])

print("".join(l),end="")
print("".join(reversed(r)))