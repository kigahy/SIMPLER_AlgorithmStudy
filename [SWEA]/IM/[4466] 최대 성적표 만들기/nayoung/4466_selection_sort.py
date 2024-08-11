# SWEA. 4466 최대 성적표 만들기

'''
당신은 N개의 과목에 대한 시험을 쳤다. 각 과목의 점수는 정수이고 만점은 100점이다.

성적표에는 이 중에서 정확히 K개의 과목을 선택하여 넣을 수 있다. 당신은 기왕이면 성적표에 나타나는 총점이 가장 크도록 성적표를 만들고 싶다.

최대로 만들 수 있는 총점은 몇점인지 구하여라.


 [입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 N,K(1≤K≤N≤100)이 공백 하나로 구분되어 주어진다.

두 번째 줄에는 N개의 정수가 공백 하나로 구분되어 주어진다. 각 정수는 0 이상 100이하이다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 성적표에 표시될 총점의 최댓값을 출력한다.

'''


def selection_sort(N, score):  # 내림차순으로 선택정렬하는 selection_sort 함수

    for i in range(N):
        max_idx = i  # 기준 인덱스
        for j in range(i + 1, N):
            if score[max_idx] < score[j]:  # 기준인덱스보다 그 뒤에있는 값들 비교했을 때 크면
                max_idx = j  # 기준 인덱스 재할당
        score[i], score[max_idx] = score[max_idx], score[i]  # 기준으로 삼았던 것과 교환
    return score


T = int(input())  # 테스트 케이스 수

for case in range(1, T + 1):
    N, K = map(int, input().split())  # N : 과목 갯수  K : K개의 과목만큼 최대성적 넣기 가능
    score = list(map(int, input().split()))
    max_hap = 0  # 최대값 닮을 합 변수 초기 설정

    for sc in range(K):
        max_hap += selection_sort(N, score)[sc]  # 선택정렬한 함수 사용시 결과 : [100, 90, 80]  => 이중에서 K만큼 반복해서 앞에서 부터 값 더해줌
    print(f'#{case} {max_hap}')