'''
이 문제 dfs로 접근하여 풀다가 재귀 무한루프에 빠져서..
bfs로 풀었습니다...
큐로 해서 pop했는데 테케 2개가 런타임에러났는데 deque쓰니까 통과...ㅎ
이렇게 시간복잡도에 대해 생각하게되었습니두..
'''

from collections import deque

def solution(numbers, target):
    answer = 0
    idx = -1  # 인덱스 0부터 탐색하기에 -1로 지정해줌
    hap = 0  # 합 값 담아줌

    queue = deque([(idx, hap)])

    while queue:  # 큐가 빌때까지 진행
        i, v = queue.popleft()   # i : 인덱스 , v : 각 인덱스에 해당하는 value값
        i += 1
        if i == len(numbers) and v ==target:  # i가 numbers길이 만큼 왔다는건 다 탐색 했음 + target 값같으면 값 찾았다는 뜻
            answer += 1
        else:
            queue.append((i, v + numbers[i]))   # 큐에서 뽑아서 각각 요소에 대한 +, - 값하여 합한 값 다시 담아줌
            queue.append((i, v - numbers[i]))

    return answer
