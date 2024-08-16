T = int(input())

for tc in range(1, T+1) :
    N = int(input())

    plants = [list(map(int, input())) for _ in range(N)]

    middle = N//2 # 마름모가 가장 커지는 중간 행
    start = N//2 # 열의 너비 조정할 시작 인덱스
    end = N//2 # 열의 너비 조정할 마지막 인덱스

    sum = 0 # 합산 변수
    for i in range(N) : # 행 탐색
        for j in range(start, end+1) : # 열 탐색
            sum += plants[i][j] # 농작물의 합계를 저장

        if i < middle : # 만약 마름모의 위쪽이라면
            start = start-1 # 시작 범위를 앞으로 당기고
            end = end+1 # 끝나는 범위를 뒤로 늘려감

        elif i >= middle : # 만약 마름모의 아래쪽이라면
            start = start + 1 # 시작 범위를 뒤로 밀고
            end = end-1 # 끝나는 범위를 앞으로 줄임

    print(f'#{tc} {sum}')


    '''시행착오 1: 중심을 기준으로 행을 위아래로 확장, 열을 양옆으로 축소하려 함
    for i in range(0, center+1, 1) : # 중심부터 행을 확장해감. 2 -> 4
        for j in range(center+1, 0, -1) : # 중심부터 열을 줄여감. 2->0
            for k in range(j) : # 열 하나씩 순회
                print(plants[center+i][center+k], plants[center-i][center-k])
                sum += plants[center+i][center+k] + plants[center-i][center-k]
    '''

    '''시행착오 2: 1행부터 시작해서 열은 그대로 중간에서 확장하려 함
    for i in range(N) :
        plus = 0
        for j in range(N) : # 열 탐색
            for k in range(middle) :
                if k == 0 :
                    sum += plants[i][middle]
                else :
                    sum += plants[i][middle-k] + plants[i][middle+k]
                    plus += 1
    for l in range(middle, 0) :
        for j in range(N):  # 열 탐색
            for k in range(middle):
                if k == 0:
                    sum += plants[i][middle]
                else:
                    sum += plants[i][middle - k] + plants[i][middle + k]
                    plus += 1
            print(sum)
    print(sum)
    '''

# 로직은 올바르게 생각하였으나 코드를 조잡하게 짰으며 결국 완성시키지 못하여 구글 검색을 활용하여 코드를 짜는 법을 알아냄. 제일 어려웠다