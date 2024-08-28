T = int(input())

for tc in range(1, T+1) :
    V, E = map(int, input().split()) # 정점 수, 간선 수
    arr = [list(map(int, input().split())) for _ in range(E)]

    S, G = map(int, input().split())


