import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    # N 수강생 수 , K 과제를 제출한 사람 수
    N, K = map(int, input().split())
    # 과제를 제출한 사람의 번호 K개의 리스트
    submit_lst = list(map(int, input().split()))

    # 만약 N이 5이면 번호 1 2 3 4 5
    # 과제 제출한 사람 번호 2 5 3
    # 안낸 사람 1 4

    # 학생 리스트 생성
    student_lst = [i for i in range(1, 1+N)]
    no_submit = []

    for student in student_lst:
        if student not in submit_lst:
            # 제출한 애가 아니면 리스트 추가
            no_submit.append(student)

    print(f'#{tc} {" ".join(list(map(str, no_submit)))}')
