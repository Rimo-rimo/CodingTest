def solution(progresses, speeds):
    re = []
    for i,k in zip(progresses, speeds):
        if (100 - i) % k == 0:
            re.append((100 - i)//k)
        else:
            re.append((100 - i)//k + 1)
    result = []
    while True:
        count = 0
        for i in range(len(re)):
            if re[0] >= re[i]:
                count += 1
            else:
                result.append(count)
                re = re[i:]
                count = 0
                break
        if count != 0:
            result.append(count)
            break
            
    return result