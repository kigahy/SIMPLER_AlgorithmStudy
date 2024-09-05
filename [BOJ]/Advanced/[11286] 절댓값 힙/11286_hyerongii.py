# heapq 모듈 사용
import heapq

# 절대값 힙 리스트에 절대 값 처리한 값이랑 원래 값이랑 같이 넣어주기
abs_heap = []
n = int(input())
for i in range(n):
    num = int(input())
    # 0 이 아니면 넣어줘서 힙 처리하기
    if num:
        heapq.heappush(abs_heap, (abs(num), num))
    # 0 이면
    else:
        # 절대값 힙 리스트에서 원래값 뽑아주기
        if abs_heap:
            print(heapq.heappop(abs_heap)[1])
        # 뽑을거 없으면 0
        else:
            print(0)
