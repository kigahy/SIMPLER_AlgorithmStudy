# 제가 접해본 BFS인 SWEA 5102의 코드 템플릿을 따서 풀어보려 했습니다
# 그런데 실패하였고 풀다가 만 코드입니다
# BFS 풀이 방식도 다양하다는 것을 알게 된 문제입니다

def back(i, count) : # 나름대로 백트래킹 해보려고 시도한 흔적(...)
    if numbers[i] + numbers[i+1] == target : # 계산했을 때 target과 맞다면
        return count
    elif numbers[i] - numbers[i+1] == target :
        return count
    else :
        return i, count
def solution(numbers, target): # 리스트와 만들 값
    global order # 현재 인덱스
    global count # 횟수

    count += 1 # 한번 계산하였으므로 1 추가
    q = [(order, count)] # 인덱스와 횟수로 튜플 형성
    while q : # 큐에 값이 남아있을 때까지 반복
        num = q.pop(0) # 현재 순서와 카운트
        index = num[0] # 현재 인덱스값
        count = num[1] # 몇번 갔는지 count에 저장

        for i in range(index, len(numbers)+1) : # 현재 인덱스부터 끝까지 반복하며 계산
            back(i, count)

for tc in range(2) :
    numbers = list(map(int, input().split())) # 숫자 입력
    target = int(input()) # 만들고자 하는 값
    order = 0  # 현재 리스트의 순서
    count = 0 # 횟수

    result = solution(0, target)
    print(f'#{tc} {result}')