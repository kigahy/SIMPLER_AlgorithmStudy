T = int(input())  # 테스트 케이스 수

for case in range(1, T + 1):

    N, K = map(int, input().split())  # N : 과목의 개수 K : 최대 합에 넣을 과목의 갯수
    score = list(map(int, input().split()))
    max_hap = 0  # 선택한 과목 갯수 최대합 담아줄 변수 초기값 설정

    score.sort(reverse=True)  # 성적 점수들 내림차순으로 정렬   [100, 90, 80]

    for sc in range(K):  # 선택할 K만큼 hap에 더해줌
        max_hap += score[sc]
    print(f'#{case} {max_hap}')