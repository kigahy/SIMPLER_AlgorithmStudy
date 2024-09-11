"""
begin = "hot"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
begin에서 target을 만드는 데 한 번에 한 알파벳만 바꿀 수 있습니다.
저는 문제를 보고, 단어들을 비교하며 한 글자 씩 달라지는 경우 끼리 연결하여 그래프를 만들었습니다.
그렇게 그래프를 만들어 BFS를 통해 begin에서 target까지 최단 거리를 구해야겠다고 접근했습니다.
"""

from collections import deque


def solution(begin, target, words):
    answer = 0  # begin에서 target까지의 최단 거리
    word_dict = {}  # 인접 리스트를 표현할 딕셔너리
    words.append(begin)  # 한 알파벳만 차이나는 경우를 구하기 위해 words에 begin을 포함시킨다.
    N = len(words)

    visited = set()  # 이미 방문한 곳을 제외하기 위한 visited set
    dist = {}   # 거리를 기록하기 위한 딕셔너리

    def word_change(start):
        visited.add(start)  # 시작점(begin) 방문 표시
        dist[start] = 0  # 시작점은 거리가 0
        queue = deque()
        queue.append(start)

        while queue:
            next_word = queue.popleft()
            for word in word_dict[next_word]:
                if word in visited: continue
                visited.add(word)
                queue.append(word)
                dist[word] = dist[next_word] + 1

    for word in words:
        word_dict[word] = []
        dist[word] = 0
        for comp in words:
            if word == comp: continue
            cnt = 0
            for i in range(len(begin)):
                if word[i] != comp[i]:
                    cnt += 1
                if cnt > 1: continue
            else:
                if cnt == 1:
                    word_dict[word].append(comp)

    # print(word_dict)
    # print(dist)
    word_change(begin)
    if target not in words:
        answer = 0
    else:
        answer = dist[target]

    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
