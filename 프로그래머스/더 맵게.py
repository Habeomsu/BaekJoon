import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville)>1:
        if scoville[0]>=K:
            break
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + second *2
        heapq.heappush(scoville,new)
        answer +=1
    if len(scoville)==1:
        if scoville[0] <K:
            return -1
    return answer

'''

힙 배열을 만든다.
힙 팝을 2번해서 새로운 값을 만든다.
새로운 값을 힙에 접어넣는다.
모든 수가 K이상일때 까지 반복한다.


'''