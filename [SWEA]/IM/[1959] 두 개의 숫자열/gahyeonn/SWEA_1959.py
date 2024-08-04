T = int(input())

for test_case in range(1, T+1) :
    small, big = map(int, input().split())

    up = list(map(int, input().split()))
    down = list(map(int, input().split()))

    if small > big :
        big, small = small, big
        up, down = down, up
    elif small < big :
        pass

    max_val = 0
    for i in range(big-small+1) :
        #val += up[i] * down[i]
        val = 0
        for j in range(small) :
            val += up[j] * down[i+j]
        if val > max_val :
            max_val = val
 
    print(f'#{test_case} {max_val}')
