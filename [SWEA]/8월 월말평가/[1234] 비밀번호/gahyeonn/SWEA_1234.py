for tc in range(1, 11) :
    N, string = input().split() # str형태로 받아옴
    stack = [] # 중복 검사할 스택

    for item in string : # string에 직접 접근
        if stack and stack[-1] == item : # 스택 마지막 값과 새 값을 비교하며 중복 검사
            stack.pop() # 중복된다면 스택에서 제거

        else :
            stack.append(item) # 중복되지 않다면 stack에 추가

    print(f'#{tc} {"".join(stack)}') # 비밀번호 완성

    # 조건문에 추가했다가 빠꾸먹고 else만 입력한 코드들입니다.
    #
    # elif stack and stack[-1] != item:
    # stack.append(item)
    #
    # elif not stack:
    # stack.append(item)