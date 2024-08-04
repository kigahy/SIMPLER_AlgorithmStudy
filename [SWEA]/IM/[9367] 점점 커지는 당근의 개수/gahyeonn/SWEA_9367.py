T = int(input())

for test_case in range(1, T+1) :
    carrot = int(input())

    scale = list(map(int, input().split()))

    max = 0
    count = 0
    lst = []
    j = 0
    for i in range(1, carrot) :
        if scale[i] - scale[i-1] == 1 :
            count += 1
            max = scale[i]
        else :
            count = 0



    print(max(lst))

