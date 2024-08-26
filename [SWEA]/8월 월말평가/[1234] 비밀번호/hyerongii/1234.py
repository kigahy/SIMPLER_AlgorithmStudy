import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T+1):
    N, string = input().split()
    # 입력받은 N int로 변경, 번호 문자열은 str list 상태로 두기
    N = int(N)
    string = list(string)
    # stack 사용하여 좌우 번호가 같은 번호인지 확인 후 소거하기
    stack = []

    for i in range(N):
        if not stack or stack[-1] != string[i]:
            stack.append(string[i])
        elif stack and stack[-1] == string[i]:
            stack.pop()
    # 남은 번호들이 비밀번호가 된다
    print(f'#{tc} {"".join(stack)}')
