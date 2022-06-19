def solution(record):
    dic = {}
    re = []
    for i in record:
        sentence = i.split()
        re.append(sentence)
        if sentence[0] in ["Enter", "Change"]:
            dic[sentence[1]] = sentence[2]
    result = []
    for i in re:
        if i[0] == "Enter":
            result.append(f"{dic[i[1]]}님이 들어왔습니다.")
        if i[0] == "Leave":
            result.append(f"{dic[i[1]]}님이 나갔습니다.")
        
    return result