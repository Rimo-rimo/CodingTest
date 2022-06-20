# 수학적 방법론으로 풀어봤을때
n,m,k = map(int, input().split())
data = sorted(list(map(int,input().split())), reverse=True)

n_1 = m//(k+1)
n_2 = m%(k+1)

result = n_1*(data[0]*k + data[1]) + n_2*data[0]
print(result)


# n, m, k = map(int,input().split())
# re = sorted(list(map(int,input().split())), reverse=True)
# cnt = 0
# result = 0
# while cnt != m:
#     if re[0] == re[1]:
#         result += m*re[0]
#         cnt = m
#     else:
#         if (m - cnt) <= k:
#             result += (m - cnt)*now
#             cnt += (m - cnt)
#         else:
#             result += k*re[0] + re[1]
#             cnt += (k + 1)
# print(result)




