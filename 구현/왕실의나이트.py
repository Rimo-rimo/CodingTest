a = input()
W = "abcdefgh".find(a[0]) + 1
H = int(a[1])
cnt = 0

move = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
for i in move:
    w = W + i[0]
    h = H + i[1]
    if w <= 8 and w >= 1:
        if h <= 8 and h >= 1:
            cnt += 1
print(cnt)


# if w >= 3 and w <= 6:
#     if h >= 3 and h <=6:
#         result = 8
#     elif h in [2,7]:
#         result = 6
#     else:
#         result = 4 
# elif w in [2,7]:
#     if h >= 3 and h <=6:
#         result = 4
#     elif h in [2,7]:
#         result = 6
#     else:
#         result = 3
# else:
#     if h >= 3 and h <=6:
#         result = 4
#     elif h in [2,7]:
#         result = 3
#     else:
#         result = 2
# print(result)



