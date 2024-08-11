T = int(input())  # 테스트 케이스 수

for case in range(1, T + 1):
    N, K = map(int, input().split())  # N : 수강생 수 , K : 과제 제출한 학생 수
    submit_num = list(map(int, input().split()))  # 과제 제출한 번호

    check_submit = [0] * (N + 1)  # 냈는지 확인하기 위한 빈배열 생성

    for i in range(K):
        for j in range(1, N + 1):  # 학생 번호는 1부터 시작하기에 0은 제외 하여 순회
            if submit_num[i] == j:  # 제출한 학생의 리스트 순회하면서 1~5중에 같으면
                check_submit[j] = 1  # check_submit 인덱스 활용하여 제출한 학생 번호(=인덱스)에 체크 "1" 표시

    print(f'#{case}', end=' ')

    for not_chek in range(1, N + 1):
        if check_submit[not_chek] == 0:  # 제출하지 않은 학생 인덱스 == 제출 안한 사람의 번호
            print(not_chek, end=' ')
    print()