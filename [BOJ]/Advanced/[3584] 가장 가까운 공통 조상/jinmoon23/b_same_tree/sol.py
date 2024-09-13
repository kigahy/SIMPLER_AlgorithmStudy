'''
루트가 있는 트리가 주어지고, 두 노드가 주어질 때 그 두 노드의 가장 가까운 공통 조상을 찾는 프로그램을 작성하세요
테스트 케이스의 마지막 줄에 가장 가까운 공통 조상을 구할 두 노드가 주어집니다.

접근법(1번 테케)
1. 16을 자식으로 가지는 부모인덱스 식별(10) / 7을 자식으로 가지는 부모인덱스 식별(6)
2. 1의 부모인덱스 2개를 동시에 자식으로 가지는 조상인덱스 식별 및 리턴

2번 테케
1. 3을 자식으로 가지는 부모인덱스 식별(2) / 5를 자식으로 가지는 부모인덱스 식별(1)
2. 1의 부모인덱스 2개를 동시에 자식으로 가지는 조상인덱스 식별 -> 없음!
3. 트리 형태로 나타내면 아래와 같음. 2가 3과 5의 공통조상이긴 하지만 더 깊은 뎁스인 3도 공통조상이기 때문에 3을 리턴해야 함.
4. 자기 자신(3)이 자기 자신의 부모이자 조상이다..? -> 이런 유형의 문제에서 대체로 전제하는 약속 같은 것.
    2
    |
    3
4       1
            5

2번의 3,5는 3이 1의 부모이면서 1이 5의 부모 -> 일자로 이어지는 형태


그럼 1번 테케도 "자기 자신이 자기 자신의 조상이다" 라는 전제를 기반으로 접근법을 달리해야 함.

접근법
1. 일자로 이어지는 형태의 경우 그 형태의 가장 루트노드의 값을 리턴
2. 그렇지 않은 경우

'''

import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def recur(target1,target2):
    # 1. 종료조건 설정
    # 공통의 조상이 발견된 일반적인 경우
    if tree[target1] == tree[target2]:
        print(*tree[target1])
        return
    # 테케2의 경우
    elif tree[target2][0] == t1:
        print(t1)
        return
    # 테케2와 비슷한 경우 대비
    elif tree[target1][0] == t2:
        print(t2)
        return
    # 2. 재귀호출
    recur(*tree[t1],*tree[t2])

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 노드의 개수
    E = N - 1
    E_infos = [list(map(int, input().split())) for _ in range(N)]
    find = E_infos.pop()
    tree = [[] for _ in range(N+1)]

    # 1. 인덱스를 자식노드로 / 값을 부모노드로 구성
    for info in E_infos:
        p,c = info[0],info[1]
        tree[c].append(p)

    print(tree) # [[], [8], [10], [16], [8], [8], [4], [6], [], [5], [4], [10], [16], [1], [1], [6], [10]]

    t1,t2 = find
    recur(t1,t2)