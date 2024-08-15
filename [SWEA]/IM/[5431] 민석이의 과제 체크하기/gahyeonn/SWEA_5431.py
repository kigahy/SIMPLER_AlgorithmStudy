T = int(input())

for tc in range(1, T+1) :
    all_stu, submit_stu = map(int, input().split()) # 총 학생 수, 제출한 학생 수
    submit_num = list(map(int, input().split())) # 제출한 학생의 번호

    all_num = [all_stu for all_stu in range(1, all_stu+1)] # 모든 학생의 번호를 1부터 생성
    not_num = [] # 안낸 한생 번호를 추가

    for i in all_num : # 모든 학생의 번호만큼 반복
        for j in submit_num : # 제출한 학생의 번호만큼 반복
            if i == j : # 만약 제출했다면
                break # 2중 for문 깨트리고 모든 학생의 번호 중 다음 번호 검사
            else : # 2중 for문에서 제출하지 않았다면
                continue # 2중 for문의 다음 숫자 순회
        else: # for문의 break가 걸리지 않으면 실행되며, i가 submit_number에 해당되지 않았을 때
            not_num.append(i) # 쓰고 싶지 않았지만 써버린 append

    print(f'#{tc} {" ".join(map(str, not_num))}')

# 아쉬운 점 : 슬프게도 for-else 없이는 이 코드를 완성할 수 없었음.
# 나는 왜 all_num을 만들었을까? 내 생각의 한계

