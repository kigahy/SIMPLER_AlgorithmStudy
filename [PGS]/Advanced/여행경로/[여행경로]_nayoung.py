def solution(tickets):
    def dfs(start, ans):

        for i in range(len(road_dict[start])):
            if road_dict[start][i] not in road_dict.keys():
                ans.append(road_dict[start][i])
                return

            if visited[start][i]:
                continue
            visited[start][i] = 1
            ans.append(road_dict[start][i])
            dfs(road_dict[start][i], ans)


    ans = []
    start = "ICN"
    road_dict = {}  # {'ICN': ['JFK'], 'HND': ['IAD'], 'JFK': ['HND']}
    visited = {}

    for s, v in tickets:
        if s in road_dict:
            road_dict[s].append(v)
            visited[s].append(0)
        else:
            road_dict[s] = [v]
            visited[s] = [0]

    for key in road_dict.keys():  # 문제에서 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로 return 위해 sort작업처리
        road_dict[key].sort()
    # {'ICN': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}

    ans.append(start)  # 인천 출발

    dfs(start, ans)

    return ans