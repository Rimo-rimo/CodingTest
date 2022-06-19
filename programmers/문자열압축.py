def solution(s):
    n = 1
    result = [len(s)]
    while n <= len(s)/2:
        re = ""
        wrd = s[:n]
        cnt = 0
        for i in range(0,len(s),n):
            try:
                r = s[i:i+n]
                if r == wrd:
                    cnt += 1
                else:
                    if cnt != 1:
                        re += str(cnt) + wrd
                    else:
                        re += wrd
                    cnt = 1
                    wrd = r
            except:
                r = s[i:]
                re += r
        if cnt != 1:
            re += str(cnt) + r
        else:
            re += wrd
        result.append(len(re))
        n += 1
            
    return min(result)









































# def solution(s):
#     result = [len(s)]
#     for i in range(1,len(s)//2 + 1):
#         re = []
#         ss = s
#         while len(ss) >= i:
#             re.append(ss[0:i])
#             ss = ss[i:]
#         if len(ss) != 0:
#             re.append(ss)
#         count = 1
#         num = ""
#         for k in range(len(re)):
#             try:
#                 if re[k] == re[k+1]:
#                     count += 1
#                 else:
#                     if count == 1:
#                         num += re[k]
#                     else:
#                         num += (str(count) + re[k])
#                         count = 1
#             except:
#                 if count == 1:
#                     num += re[k]
#                 else:
#                     num += (str(count) + re[k])
#         result.append(len(num))
                    
            
#     return min(result)