import sys # 제출 전 반드시 삭제할 것
sys.stdin = open('sample_input.txt', 'r') # 제출 전 반드시 삭제할 것

T = int(input())
for test_case in range(1, T + 1):

    AnswerN = 0 # LED 바뀐 횟수

    N = int(input()) # 전구 수
    data = [int(num) for num in input().split()] # 바꾸고자 제시된 LED

    #######################################################################################################
    change = [0]*N # 하나씩 바꿔나갈 LED
    boolean = False # 한줄.

    for i in range(len(data)) : # data의 개수만큼 돌며 i를 통해 인덱스에 접근

        if data[i] == 1 and change[i] == 0 : # 원하는 리스트가 1이고 아직 1로 안바꼈다면
            for j in range(i, len(change), i+1) : # data 인덱스+1의 배수 인덱스만큼 바꿈
                if change[j] == 0 :
                    change[j] = 1
                elif change[j] == 1 :
                    change[j] = 0
            #print(change) # 디버깅
            #AnswerN += 1
            boolean = True

        if data[i] == 0 and change[i] == 1 : # 원하는 리스트가 1이고 아직 1로 안바꼈다면
            for j in range(i, len(change), i+1) : # data 인덱스+1의 배수 인덱스만큼 바꿈
                if change[j] == 0 :
                    change[j] = 1
                elif change[j] == 1 :
                    change[j] = 0
                #change[j] = 0
            #print(change)  # 디버깅
            #AnswerN += 1
            boolean = True

        if boolean == True :
            AnswerN += 1
            boolean = False

        #else : # 원하는 리스트가 0이거나, 원하는 리스트가 1이지만 이미 1이라면
        #    continue # 다음 리스트를 순회함
    '''
    for k in range(len(change)) :
        if data[k] != change[k] :
            change[k] = 0
            AnswerN += 1
        else :
            continue
    '''

    #print(change)


    #######################################################################################################

    # 표준출력(화면)으로 답안을 출력합니다.
    print("#%d %d" % (test_case, AnswerN))


    #for i in range(len(data)) : # data의 개수만큼 돌며 i를 통해 인덱스에 접근
    #    if data[i] == 1 and change[i] == 0 : # 원하는 리스트가 1이고 아직 1로 안바꼈다면
    #        for j in range(len(change)) :


    #for k in range(len(change)) :
    #    if data[i] != change[i] :
    #        change[i] = 0
    #        AnswerN += 1
    #    else :
    #        continue