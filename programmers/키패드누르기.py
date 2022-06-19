def get_num(num, L, R, hand):
    table = {2:[3,1,0,1,2,1,2,3,2,3,4,4],5:[2,2,1,2,1,0,1,2,1,2,3,3],
             8:[1,3,2,3,2,1,2,1,0,1,2,2],0:[0,4,3,4,3,2,3,2,1,2,1,1]}
    table = table[num]
    L = table[L]
    R = table[R]
    if L > R:
        return "R"
    elif L < R:
        return "L"
    else:
        if hand == "right":
            return "R"
        else:
            return "L"

def solution(numbers, hand):
    L = 10
    R = 11
    result = ""
    two = {}
    
    for i in numbers:
        if i in [1,4,7]:
            result += "L"
            L = i
        elif i in [3,6,9]:
            result += "R"
            R = i-2
        else:
            h = get_num(i, L, R, hand)
            if h == "L":
                L = i
            else:
                R = i
            result += h
            
        
    return result






def solution(numbers, hand):
    L = [1,4,7]
    R = [3,6,9]
    result = []
    nums = {2:{1:1,2:0,3:1,4:2,5:1,6:2,7:3,8:2,9:3,0:3,"*":4,"#":4},5:{1:2,2:1,3:2,4:1,5:0,6:1,7:2,8:1,9:2,0:2,"*":3,"#":3},8:{1:3,2:2,3:3,4:2,5:1,6:2,7:1,8:0,9:1,0:1,"*":2,"#":2}, 0:{1:4,2:3,3:4,4:3,5:2,6:3,7:2,8:1,9:2,0:0,"*":1,"#":1}}
    L_now = "*"
    R_now = "#"
    for i in numbers:
        if i in [1,4,7]:
            result.append("L")
            L_now = i
        if i in [3,6,9]:
            result.append("R")
            R_now = i
        if i in [2,5,8,0]:
            l = nums[i][L_now]
            r = nums[i][R_now]
            if l > r:
                result.append("R")
                R_now = i
            if l < r:
                result.append("L")
                L_now = i
            if l == r:
                if hand == "right":
                    result.append("R")
                    R_now = i
                else:
                    result.append("L")
                    L_now = i
            
    return "".join(result)