# 4881. 배열 최소 합

'''
이 문제는 풀다가 너무 어려워서 다른사람 코드 참조하여 푼 문제입니다..
다시 도전할 계획입니다!
'''
def min_hap(x, sum_v):
    global min_sum

    if sum_v >= min_sum:  # 백트래킹 사용 만약 선택한 합들이 min_sum보다 크면 더이상 탐색 안해도 되니 리턴
        return

    if x == N:  # 행이 N과 같아졌다는 뜻은 끝까지 탐색했다는 뜻
        if min_sum > sum_v:  # 최소값 비교
            min_sum = sum_v  # 최소값 재할당
            return

    for col in range(N):   # 열 선택 탐색
        if visited_row[col] == 0:   #  선택한 것과 안겹치기 위해 / 0이라는 건 선택하지 않았다는 뜻
            visited_row[col] = 1  # 열을 사용했다고 표시
            min_hap(x+1, sum_v+arr[x][col])  # 재귀호출 (다음 row 탐색 위해 row+1, 선택당한 열의 그 전 값에 값 더해주고 반환)
            visited_row[col]=0   # 방문했던건 다시 방문 원상복구 해줌 (설정 안하면 이미 체크 되어있기때문에 선택 불가능하기 때문에 꼭 필요한 과정!)

T = int(input())  # 테스트 케이스 수

for case in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    visited_row = [0]*N  # 방문 행 표시
    min_sum = N*10  # 문제에서 3<=N<=10 조건 제시 해줌 모두가 10을 선택하여 최대 합은 N*10 최소값 비교대상 선정 위함
    sum_v= 0   # sum_value 변수 초기 설정  합 담기 위함

    min_hap(0,sum_v)  # 배열의 최소 합을 구해주는 함수 호출

    print(f'#{case} {min_sum}')