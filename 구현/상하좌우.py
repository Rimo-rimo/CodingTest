N = int(input())
data = input().split()
now = [1,1]

def move(now, loc, N):
    if loc == "R":
        if now[1] == N:
            return now
        else:
            now[1] += 1
    if loc == "L":
        if now[1] == 1:
            return now
        else:
            now[1] -= 1
    if loc == "U":
        if now[0] == 1:
            return now
        else:
            now[0] -= 1
    if loc == "D":
        if now[0] == N:
            return now
        else:
            now[0] += 1
    return now


for i in data:
    move(now, i, N)
print(now)

