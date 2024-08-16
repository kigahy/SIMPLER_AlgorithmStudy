T = int(input())

for tc in range(1, T+1) :
    all_subject, select_subject = map(int, input().split()) # 모든 과목수와 선택 과목수 입력받음
    score = list(map(int, input().split()))
    total_score = 0

    for i in range(all_subject) : # 정렬 시작
        for j in range(all_subject - i - 1) :
            if score[j] < score[j+1] : # 내림차순
                score[j], score[j+1] = score[j+1], score[j]

    for k in range(select_subject) : # 내림차순 정렬한 리스트만큼 반복
        total_score += score[k] # 리스트 앞부터 합 구함

    print(f'#{tc} {total_score}')

# 버블정렬 방식을 선택했고, 구글 검색을 통하여 버블소트 활용함 ㅠㅠ 혼자 구현하는 방법 외워둬야지
# 버블정렬 방식이 교재와 좀 다른데, 다양한 방식으로 구현할 수 있음을 알게 되었음!