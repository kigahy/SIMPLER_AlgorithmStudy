import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    # N 점수 개수 K 과목 개수
    N, K = map(int, input().split())
    score_lst = list(map(int, input().split()))

    # K 개 선택했을 때 제일 큰 점수 리턴
    total = 0
    # K 번 만큼 리스트에서 큰 수 뽑아내기
    for _ in range(K):
        max_s = score_lst[0]
        # 리스트에서 제일 큰 값 찾기
        for score in score_lst:
            if score > max_s:
                max_s = score
        # 찾으면 없애고 total에 더해주기 이과정 K만큼 반복
        score_lst.remove(max_s)
        total += max_s

    print(f'#{tc} {total}')



