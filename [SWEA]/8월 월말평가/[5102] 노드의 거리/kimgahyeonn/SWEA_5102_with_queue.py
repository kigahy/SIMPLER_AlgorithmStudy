# 강사님께 여쭤보고 받은 코드이며, BFS 방식입니다.

import sys
sys.stdin = open('input.txt')


def BFS(n, count):
    q = [(n, count)]
    visited[n] = 1
    while q:
        target = q.pop(0)
        n = target[0]
        count = target[1]
        # n, count = q.pop(0)
        for w in range(1, V+1):
            if mat[n][w] and not visited[w]:
                if w == G:
                    return count + 1
                visited[w] = 1
                q.append((w, count + 1))


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    mat = [[0] * (V+1) for _ in range(V+2)]
    visited = [0] * (V+2)
    for info in arr:
        mat[info[0]][info[1]] = 1
        mat[info[1]][info[0]] = 1
    count = BFS(S, 0)
    print(f'#{tc} {count}')
