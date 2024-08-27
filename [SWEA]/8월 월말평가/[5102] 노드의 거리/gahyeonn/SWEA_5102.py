T = int(input()) # 테스트케이스 10개중에 5개만 맞음

def dfs(s, G) :
    global count # for문에서 선언한 count 변수를 전역으로 사용하겠다는 뜻
    stack = [] # 순회하다 되돌아갈 부모노드를 저장할 것
    visited = [0] * (V+1) # 정점의 인덱스 번호로 방문했느냐를 판단
    visited[s] = 1 # 시행착오. 이것도 안적었음
    v = s # 위치에 주의
    
    while True :
        # 시행착오. 여기에 v = s 하고 오류났음
        for w in data[v] : # 부모노드의 자식노드를 순회
            if visited[w] == 0 : # 만약 해당 노드의 인접 노드를 방문하지 않았다면
                # visited[v] = 1 # 시행착오. 위치에 주의! 그 부모노드를 1로 처리한 후
                stack.append(v) # 부모노드의 번호를 stack에 저장
                v = w # 자식 노드를v로 만들고 탐색 시작할 준비
                visited[v] = 1 # 그 부모노드를 1로 처리한 후 <- 아님. 새 탐색 시작과 동시에 방문체크 하는 것임.
                count += 1 # G와 연결된 간선 하나를 이동했으니 1 증가
                break # !주의! 난 여기 break 넣는지 몰랐음. w를 모두 돌고 나면 부모의 또다른 인접노드를 탐색하러 떠남 
            
            # 시행착오. 뭐야 이게 왜 안되지...?
            # elif visited[w] == 1 : # 만약 해당 노드의 인접 노드를 이미 방문했다면
            #     v = stack.pop() # 미리 저장해둔 부모노드를 순회하기를 시도함
            #     break # for문을 빠져나오고, 해당 부모노드의 자식노드는 모두 보았으니 다음 부모노드를 순회함
        
        else : # 만약 위의 구문이 실행되지 않았다면? 위 조건과 해당되지 않는다면 for문도 빠져나와
            if stack : # 스택에 값이 남아있다면 돌아갈 부모가 있다는 뜻
                v = stack.pop()
                count -= 1 # 돌아갈 부모가 있다는 건 온 길을 다시 돌아가므로, count를 1씩 뺌
            else : # 스택에 값도 없고 연결된 값도 없다는 뜻. GG
                break

        if v == G : # 시작점부터 끝 노드까지 다 돌면 
            return count
    return 0 # 시작점과 끝점이 연결되지 않았다면 0 리턴

for tc in range(1, T+1) :
    V, E = map(int, input().split()) # 정점 수, 간선 수
    arr = [list(map(int, input().split())) for _ in range(E)] # 간선 양쪽의 노드 번호
    S, G = map(int, input().split()) # 출발 노드, 도착 노드

    count = 0 # 간선 이동하는 숫자 셀 변수 선언
    # data = [list(map(int, input().split())) for _ in range(E)] 시행착오. range(E) 아니고 range(V+1)
    data = [[] for _ in range(V+1)] # 해당 인덱스 번호에 해당하는 노드의 인접 노드가 몇개인지 모르니 []로 선언

    for i in range(E) : # 각 하나의 간선에 대하여
        v1 = arr[i][0] # 시작 정점의 값
        v2 = arr[i][1] # 끝나는 정점의 값
        
        data[v1].append(v2) # 인덱스 번호로 인접 노드 찾기 위하여 저장
        data[v2].append(v1)

    result = dfs(S, G)
    print(f'#{tc} {result}')

'''
T = int(input())

def dfs(s, G) :
    global count # for문에서 선언한 count 변수를 전역으로 사용하겠다는 뜻
    visited[s] = 1 # 시행착오. 이것도 안적었음
    v = s # 위치에 주의
    
    while True :
        # 시행착오. 여기에 v = s 하고 오류났음
        for w in data[v] : # 부모노드의 자식노드를 순회
            if visited[w] == 0 : # 만약 해당 노드의 인접 노드를 방문하지 않았다면
                # visited[v] = 1 # 시행착오. 위치에 주의! 그 부모노드를 1로 처리한 후
                stack.append(v) # 부모노드의 번호를 stack에 저장
                v = w # 자식 노드를v로 만들고 탐색 시작할 준비
                visited[v] = 1 # 그 부모노드를 1로 처리한 후 <- 아님. 새 탐색 시작과 동시에 방문체크 하는 것임.
                count += 1 # G와 연결된 간선 하나를 이동했으니 1 증가
                break # !주의! 난 여기 break 넣는지 몰랐음. w를 모두 돌고 나면 부모의 또다른 인접노드를 탐색하러 떠남 
            
            # 시행착오. 뭐야 이게 왜 안되지...?
            # elif visited[w] == 1 : # 만약 해당 노드의 인접 노드를 이미 방문했다면
            #     v = stack.pop() # 미리 저장해둔 부모노드를 순회하기를 시도함
            #     break # for문을 빠져나오고, 해당 부모노드의 자식노드는 모두 보았으니 다음 부모노드를 순회함
        
        else : # 만약 위의 구문이 실행되지 않았다면? 위 조건과 해당되지 않는다면 for문도 빠져나와
            if stack : # 스택에 값이 남아있다면 돌아갈 부모가 있다는 뜻
                v = stack.pop()
                count -= 1 # 돌아갈 부모가 있다는 건 온 길을 다시 돌아가므로, count를 1씩 뺌
            else : # 스택에 값도 없고 연결된 값도 없다는 뜻. GG
                count = 0 # 연결된 값 없으니 카운트는 0이 됨
                break

        if v == G : # 시작점부터 끝 노드까지 다 돌면 
            return count

for tc in range(1, T+1) :
    V, E = map(int, input().split()) # 정점 수, 간선 수
    arr = [list(map(int, input().split())) for _ in range(E)] # 간선 양쪽의 노드 번호
    S, G = map(int, input().split()) # 출발 노드, 도착 노드

    count = 0 # 간선 이동하는 숫자 셀 변수 선언
    stack = [] # 순회하다 되돌아갈 부모노드를 저장할 것
    visited = [0] * (V+1) # 정점의 인덱스 번호로 방문했느냐를 판단
    # data = [list(map(int, input().split())) for _ in range(E)] 시행착오. range(E) 아니고 range(V+1)
    data = [[] for _ in range(V+1)] # 해당 인덱스 번호에 해당하는 노드의 인접 노드가 몇개인지 모르니 []로 선언

    for i in range(E) : # 각 하나의 간선에 대하여
        v1 = arr[i][0] # 시작 정점의 값
        v2 = arr[i][1] # 끝나는 정점의 값
        
        data[v1].append(v2) # 인덱스 번호로 인접 노드 찾기 위하여 저장
        data[v2].append(v1)

    result = dfs(S, G)
    print(f'{tc} {result}')
'''

'''
T = int(input())

def dfs(s, G) :
    global count # for문에서 선언한 count 변수를 전역으로 사용하겠다는 뜻
    visited[s] = 1 # 시행착오. 이것도 안적었음
    v = s # 위치에 주의
    
    while True :
        # 시행착오. 여기에 v = s 하고 오류났음
        for w in data[v] : # 부모노드의 자식노드를 순회
            if visited[w] == 0 : # 만약 해당 노드의 인접 노드를 방문하지 않았다면
                visited[v] = 1 # 그 부모노드를 1로 처리한 후
                stack.append(v) # 부모노드의 번호를 stack에 저장
                v = w # 자식 노드를v로 만듦
                count += 1 # G와 연결된 간선 하나를 이동했으니 1 증가
                break # !주의! 난 여기 break 넣는지 몰랐음. w를 모두 돌고 나면 부모의 또다른 인접노드를 탐색하러 떠남 
            
            # 시행착오. 뭐야 이게 왜 안되지...?
            # elif visited[w] == 1 : # 만약 해당 노드의 인접 노드를 이미 방문했다면
            #     v = stack.pop() # 미리 저장해둔 부모노드를 순회하기를 시도함
            #     break # for문을 빠져나오고, 해당 부모노드의 자식노드는 모두 보았으니 다음 부모노드를 순회함
        
        else : # 만약 위의 구문이 실행되지 않았다면? 위 조건과 해당되지 않는다면 for문도 빠져나와
            if stack : # 스택에 값이 남아있다면 돌아갈 부모가 있다는 뜻
                v = stack.pop()
                count -= 1 # 돌아갈 부모가 있다는 건 온 길을 다시 돌아가므로, count를 1씩 뺌
            else : # 스택에 값도 없고 연결된 값도 없다는 뜻. GG
                count = 0 # 연결된 값 없으니 카운트는 0이 됨
                break

        if v == G : # 시작점부터 끝 노드까지 다 돌면 
            return count

for tc in range(1, T+1) :
    V, E = map(int, input().split()) # 정점 수, 간선 수
    arr = [list(map(int, input().split())) for _ in range(E)] # 간선 양쪽의 노드 번호
    S, G = map(int, input().split()) # 출발 노드, 도착 노드

    count = 0 # 간선 이동하는 숫자 셀 변수 선언
    stack = [] # 순회하다 되돌아갈 부모노드를 저장할 것
    visited = [0] * (V+1) # 정점의 인덱스 번호로 방문했느냐를 판단
    # data = [list(map(int, input().split())) for _ in range(E)] 시행착오. range(E) 아니고 range(V+1)
    data = [[] for _ in range(V+1)] # 해당 인덱스 번호에 해당하는 노드의 인접 노드가 몇개인지 모르니 []로 선언

    for i in range(E) : # 각 하나의 간선에 대하여
        v1 = arr[i][0] # 시작 정점의 값
        v2 = arr[i][1] # 끝나는 정점의 값
        
        data[v1].append(v2) # 인덱스 번호로 인접 노드 찾기 위하여 저장
        data[v2].append(v1)

    result = dfs(S, G)
    print(f'{tc} {result}')
'''
