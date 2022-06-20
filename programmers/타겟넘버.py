result = 0
def dfs(numbers, target, level, son):
    global result
    if level == len(numbers) :
        if son == target:
            result += 1
        return
    plus = son + numbers[level]
    minus = son - numbers[level]
    dfs(numbers,target, level + 1, plus)
    dfs(numbers,target, level + 1, minus)

def solution(numbers, target):
    global result
    dfs(numbers,target,0,0)
    return result