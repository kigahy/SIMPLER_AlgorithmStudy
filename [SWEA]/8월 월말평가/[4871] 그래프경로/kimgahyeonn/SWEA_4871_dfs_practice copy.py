T = int(input())

def DFS(s, V) :
    visited = [0]*(V+1)
    stack = []

    v = s
    while True :
        for w in data[v] :
            if visited[w] == 0 :
                stack.append(v)
                v = w
                visited[w] = 1
                break
        else :
            if stack :
                v = stack.pop()
            else :
                break


for tc in range(1, T+1) :
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    data = [[] for _ in range(1, V+1)]

    for i in range(V+1) : # 정점의 수만큼 넣되, 한번에 2개씩 추가
        v1, v2 = arr[i*2], arr[i*2+1]
        data[v1].append(v2)
        data[v2].append(v1)

        DFS(1, V)

