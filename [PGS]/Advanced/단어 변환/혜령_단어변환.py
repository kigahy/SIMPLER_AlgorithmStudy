from collections import deque
def solution(begin, target, words):

    if target not in words:         # 타겟이 words 안에 없을때 0 반환
        return 0

    # bfs로 풀어줌
    q = deque()                     # 시작 단어 넣어주기
    q.append(begin)
    cnt = 0
    visited = [False] * len(words)  # 방문리스트 만들어주기 
                                    # 한번 체크한 words의 단어로 안되돌아가려고 만들어주었음

    while q:
        char = q.popleft()

        if char == target:          # 타겟과 현재 단어가 같으면 반환
            return cnt

        # 입력 값이 타겟과 문자 하나만 틀린경우 반환 
        # char => dog 이라면 cog 랑 문자 하나 차이나서 바로 cnt+1 하고 리턴해줌
        s = 0
        for i in range(len(target)):    # 글자수 순서대로 한개 빼고 다 같으면
            if target[i] == char[i]:
                s += 1
        if s == len(target) - 1:
            return cnt+1

        # words 에서 돌기
        for idx, word in enumerate(words):

            # 이미 방문한거 세지 x
            if visited[idx]:
                continue
            
            # 글자수 순서대로 한개 빼고 다 같으면 큐에 추가 하고 돌기
            same = 0
            for i in range(len(word)):
                if word[i] == char[i]:
                    same += 1
            if same == len(word)-1:
                q.append(word)
                visited[idx] = True
                cnt += 1
                break

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))

