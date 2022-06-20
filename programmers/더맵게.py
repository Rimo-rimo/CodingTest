import heapq as hp
def solution(scoville, K):
    hp.heapify(scoville)
    count = 0
    while scoville:
        now = hp.heappop(scoville)
        if now < K:
            if len(scoville) == 0:
                return -1
            a = now + (2*hp.heappop(scoville))
            hp.heappush(scoville,a)
            count += 1
        else:
            break
            
    return count