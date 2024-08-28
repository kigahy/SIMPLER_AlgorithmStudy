T = int(input())

def dfs(s, G) :

    while True :
        v = s
        for w in data[v] : # 부모노드의 자식노드를 순회
            if visited[w] == 0 : # 만약 해당 노드의 인접 노드를 방문하지 않았다면
                visited[v] = 1 # 그 부모노드를 1로 처리한 후
                stack.append(v) # 부모노드의 번호를 stack에 저장
                v = w # 자식 노드를v로 만듦
                break # !주의! 난 여기 break 넣는지 몰랐음. w를 모두 돌고 나면 부모의 또다른 인접노드를 탐색하러 떠남 
            
            # 시행착오. 뭐야 이게 왜 안돼...? 어려워 ㅠㅠ
            # elif visited[w] == 1 : # 만약 해당 노드의 인접 노드를 이미 방문했다면
            #     v = stack.pop() # 미리 저장해둔 부모노드를 순회하기를 시도함
            #     break # for문을 빠져나오고, 해당 부모노드의 자식노드는 모두 보았으니 다음 부모노드를 순회함
        else : # 만약 위의 구문이 실행되지 않았다면? 위 조건과 해당되지 않는다면 for문도 빠져나와
            if stack : # 스택에 값이 남아있다면 돌아갈 부모가 있다는 뜻
                v = stack.pop()
            else : # 스택에 값도 없고 연결된 값도 없다는 뜻. GG
                break

        if v == G : # 시작점과 끝점을 잇는 간선이 있다는 뜻
            return 1

for tc in range(1, T+1) :
    V, E = map(int, input().split()) # 정점 수, 간선 수
    arr = [list(map(int, input().split())) for _ in range(E)] # 간선 양쪽의 노드 번호
    S, G = map(int, input().split()) # 출발 노드, 도착 노드

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
