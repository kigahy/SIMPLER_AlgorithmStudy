'''
어떻게든 해보려고했지만..
테케1,2는 맞지만 ... 채점은 1,2번 다 틀리네요... ㅠㅠ 악질문제 완탑입니다...
제 생각 하다보니 테케에 맞춘 로직이다보니 엣지 케이스는 생각 못해서 틀린듯..?
아무튼 제 역량은 여기까지입니더...흑

'''


def solution(tickets):
    def dfs(start, ans):

        for i in range(len(road_dict[start])):  # 현재 출발지에서 갈 수 있는 모든 목적지 탐색하겠다.
            if road_dict[start][i] not in road_dict.keys():  # 목적지가 존재하지 않을 경우
                ans.append(road_dict[start][i])  # 해당 목적지 추가하고 리턴
                return

            if visited[start][i]:  # 방문하였다면 continue
                continue
            visited[start][i] = 1  # 방문 표시
            ans.append(road_dict[start][i])  # root에 목적지 추가
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