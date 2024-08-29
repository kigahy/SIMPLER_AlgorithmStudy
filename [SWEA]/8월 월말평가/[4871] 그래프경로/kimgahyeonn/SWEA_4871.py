# 이재윤 강사님의 코드를 가져와서 보고 쳤습니다. 언젠간 나 스스로 안보고 짤 날이 오기를 ㅠㅠ

T = int(input())

def dfs(s, G) :
    visited = [0] * (V+1) # 각 인덱스 번호에 해당하는 노드에 방문했는지 체크할 변수
    visited[s] = 1 # 탐색 시작과 동시에 바로 방문체크
    stack = [] # 돌아갈 노드 저장할 스택

    v = s # 자식노드 있는지 탐색할 변수 v

    while True :
        for w in data[v] : # 해당 노드(s)와 연결된 인접 노드들을 하나씩 탐색
            if visited[w] == 0 : # 만약 그 인접 노드가 방문하지 않았다면
                stack.append(v)  # 돌아올 스택에 해당 정점 인덱스 번호를 넣음
                v = w # 이제 그 인접 노드를 탐색
                visited[v] = 1 # 탐색 시작과 동시에 방문체크. 자식 노드 번호에 체크
                break # 다시 while문으로 돌아감
        else :
            if stack:
                v = stack.pop() # 방문하며 거쳐온 부모 노드를 stack에서 빼와서 위 for문에서 탐색함
            else :
                break # stack에 아무것도 없다면 모든 정점을 방문했다는 뜻이므로 종료

        if v == G : # 위 for-else문과 상관없이 새로운 노드를 탐색할 때마다 확인
            return 1 # 위 while문을 반복하다가 종료 조건인 G와 같아진다면 간선이 연결되었다는 뜻
    
    return 0 # 모든 조건식에 의해 break를 하고도 위 if문에서 return 1을 하지 못했다면 정점을 찾지 못했다는 뜻

for tc in range(1, T+1) :
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)] # 인접노드 두 개가 한 줄 띄어쓰기로 입력됨
    S, G = map(int, input().split()) # 찾는 노드의 시작점과 끝점

    data = [[] for _ in range(V+1)] 
    for i in range(E) :
        v1, v2 = arr[i][0], arr[i][1] # 각 인덱스 번호에 해당하는 노드의 인접노드를 값으로 저장
        data[v1].append(v2)

    result = dfs(S, G)
    print(f'#{tc} {result}')
    


















# 이진트리
# T = int(input())

# for tc in range(1, T+1) :
#     V, E = map(int, input().split())
#     arr = [list(map(input().split())) for _ in range(E)]

#     tree = [[0, 0] for _ in range(V+1)]

#     for i in range(V//2) :
#         parent = arr[i*2]
#         child = arr[i*2 + 1]

#         if tree[parent] == 0 :
#             tree[parent][0] = child 
#         else :
#             tree[parent][1] = child

#     print(tree)
