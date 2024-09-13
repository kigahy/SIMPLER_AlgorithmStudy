# Baek Joon. 3584 [가장 가까운 공통 조상]

# 백준 제출 코드(런타임 에러 X)

def dfs(node, root):
    while node!=0:  # node가 0이 아닐때까지 root경로 추가
        root.append(graph[node])
        node = graph[node]


T = int(input())

for case in range(1, T+1):
    N = int(input())  # 노드의 수
    arr = [list(map(int,input().split())) for _ in range(N-1)]
    a, b = map(int,input().split())  # 부모 노드를 찾아야할 두 노드
    graph = [0]*(N+1)

    a_root = [a]  # a 노드에서 시작하여 거슬러올라가는 루트 담아줌
    b_root = [b]

    for p,c in arr:   # 자식노드를 인덱스로 하여 부모노드 기록 / [0, 8, 10, 16, 8, 8, 4, 6, 0, 5, 4, 10, 16, 1, 1, 6, 10]
        graph[c] = p

    dfs(a,a_root)  # [16, 10, 4, 8]
    dfs(b,b_root) # [7, 6, 4, 8]

    for root in a_root:
        if root in b_root:  # a_root 경로 중 b_root 경로가 있다는 건 같은 조상 노드이니 break
            print(f'{root}')
            break

'''
def dfs(node, root):  # 런타임 에러남 ;;

    if graph[node] == 0:
        return

    root.append(graph[node])
    dfs(graph[node], root)

T = int(input())

for case in range(1, T+1):
    N = int(input())  # 노드의 수
    arr = [list(map(int,input().split())) for _ in range(N-1)]
    a, b = map(int,input().split())  # 부모 노드를 찾아야할 두 노드
    graph = [0]*(N+1)

    a_root = [a]
    b_root = [b]

    for p,c in arr:   # 자식노드를 인덱스로 하여 부모노드 기록 / [0, 8, 10, 16, 8, 8, 4, 6, 0, 5, 4, 10, 16, 1, 1, 6, 10]
        graph[c] = p

    dfs(a,a_root)  # [16, 10, 4, 8]
    dfs(b,b_root) # [7, 6, 4, 8]


    for root in a_root:
        if root in b_root:
            print(root)
            break
'''