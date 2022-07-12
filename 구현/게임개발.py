N, M = map(int, input().split())
A, B, d = map(int, input().split())
now = [A,B]
mapping = []
step = {0:[-1,0], 1:[0,1], 2:[1,0], 3:[0,-1]}
back = {0:[1,0], 1:[0,-1], 2:[-1,0], 3:[0,1]}
D = [0,1,2,3]
for i in range(N):
    k = list(map(int, input().split()))
    mapping.append(k)

cnt = 1
state = True
while state:
    switch = False
    for i in range(1,5):
        d = D[d-i]
        move = [now[0]+step[d][0], now[1]+step[d][1]]
        if mapping[move[0]][move[1]] == 0:
            now = [move[0], move[1]]
            cnt += 1
            mapping[move[0]][move[1]] = 1
            switch = True
            break
    if switch == False:
        move = [now[0]+back[d][0], now[1]+back[d][1]]
        if mapping[move[0]][move[1]] == 0:
            now = [move[0], move[1]]
            cnt += 1
            mapping[move[0]][move[1]] = 1
        else:
            state = False
print(cnt)






