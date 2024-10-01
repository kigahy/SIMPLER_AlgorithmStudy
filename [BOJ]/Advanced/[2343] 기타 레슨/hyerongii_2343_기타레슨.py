# 강의 개수 N, 블루레이 개수 M
# 1~5 6~7 8~9 -> 3개로 나눌 수 있음.
# 블루레이 크기 같아야함.. 합 최대한 작아야 함

N, M = map(int, input().split())

# 순서대로 입력 들어옴. 정렬시키면 틀림...뭐지..(고생함 ㅠㅠ)
guitar_lecture = list(map(int, input().split()))

# 이진탐색 - start, end, mid - 길이 합으로 생각해주기

# 가장 큰 값. 시작점
start = max(guitar_lecture)
# 마지막 값. 총합
end = sum(guitar_lecture)

result = 0
while start <= end:
    # 기준 값 중간 값
    mid = (start+end) // 2

    # 합을 계속 계산 해주기
    total = 0
    cnt = 0

    # 강의들 하나씩 합계에 더해주는데 기준 값 보다 커지면 원점으로 돌아감
    for i in range(N):
        if total + guitar_lecture[i] > mid:
            cnt += 1
            total = 0

        # 합계에 더해주기
        total += guitar_lecture[i]

    # 합계가 0보다 크면 카운트 증가
    if total > 0:
        cnt += 1

    # 개수가 M개 이거나 작으면
    if cnt <= M:
        result = mid
        # 기준점 왼쪽으로 이동
        end = mid - 1
    else:
        # 크면 기준점 오른쪽으로 이동
        start = mid + 1

print(result)


'''
이분 탐색 함수 - 반복문, while 사용 - 참고함 다시 공부함...

def binary_search(target, data)
    data.sort()
    start = 0       맨 처음 위치
    end = len(data) - 1  맨 마지막 위치
    
    while start <= end:
        mid = (start+mid) // 2
        
        if data[mid] == target:
            return mid
            
        elif data[mid] > target:
            end = mid -1
        
        else:
            start = mid + 1
    return
'''
