def maxValue(visited) :
    # 가장 멀리 떨어진 노드 찾기 위하여 최고값 추출
    maximum = 0
    total = 0
    
    # visited 중 최고값을 찾아내어 가장 먼 노드의 거리 알아냄
    for candidate in visited :
        if maximum < candidate :
            maximum = candidate
    
    # visited가 최고값일 때 가장 먼 노드의 개수 구함
    for count in visited :
        if count == maximum :
            total += 1
    return total

def BFS(node, adj_lst, start) :
    visited = [0] * len(adj_lst)
    visited[start] = 1
    queue = []
    queue.append(start)
    
    # 큐에 남은 지점 있을 때까지 반복
    while queue :
        t = queue.pop(0)
        for w in adj_lst[t] :
            if visited[w] == 0 :
                visited[w] = visited[t] + 1
                queue.append(w)
    return maxValue(visited)

def solution(n, edge):
    node = n
    
    # for문을 어떻게 짤지 고민했다
    # 간선의 수만큼 반복하여 인접리스트 형성하려고 했는데 그게 아니었다
    # edge 값에 직접 접근하여 v1과 v2를 뽑아냄
    
    adj_lst = [[] for _ in range (n+1)]
    for v1, v2 in edge :   
        adj_lst[v1].append(v2)
        adj_lst[v2].append(v1)
        
    answer = 0
    
    # 다음 코드는 for문으로 시작점 찾는 코드
    # 1번 노드와 떨어진 노드를 찾는 줄 모르고 짰다
    # for i in adj_lst :
    #     if i :
    #         start = i[0]
    #         # print(start) #디버깅
    #         break
    
    start = 1
    answer = BFS(node, adj_lst, start)
    return answer