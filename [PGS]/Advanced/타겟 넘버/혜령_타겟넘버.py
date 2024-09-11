'''
숫자들을 더할경우, 뺄경우 두가지로 나눠서 생각해주기 - 완전탐색 사용?
                    -1                                          1
          -1                   +1                     -1                   +1
      -1       +1          -1        +1          -1       +1          -1        +1
   -1   +1   -1  +1     -1   +1   -1    +1    -1   +1   -1  +1     -1   +1   -1    +1
  -1+1 -1+1 -1+1 -1+1  -1+1 -1+1 -1+1  -1+1  -1+1 -1+1 -1+1 -1+1  -1+1 -1+1 -1+1  -1+1
이런 느낌으로 계속 생길듯 ,,? 여기서 원하는 target 만드는 경우의 수 카운트
'''

def search(numbers, target, level, sum_v):
    # 함수끼리 연동되는 변수라서 둘다 글로벌 선언해줌 ㅠㅠ
    global cnt

    # 깊이 만큼 다 탐색하고, 만약 다 더해진 값이 target과 같으면 카운트
    if level == len(numbers):
        if sum_v == target:
            cnt += 1
        return

    # 더했을때
    search(numbers, target, level + 1, sum_v+numbers[level])
    # 뺐을때
    search(numbers, target, level + 1, sum_v-numbers[level])

def solution(numbers, target):
    global cnt
    cnt = 0
    search(numbers, target, 0, 0)
    answer = cnt
    return answer

# 확인용 입력 값
# arr = list(map(int, input().split()))
# target = int(input())
#
# print(solution(arr, target))