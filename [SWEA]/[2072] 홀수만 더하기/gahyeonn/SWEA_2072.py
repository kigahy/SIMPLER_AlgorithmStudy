T = int(input())

for test_case in range(1, T + 1):
    input_val = input().split(' ')
    my_list = list(map(int, input_val))
    sum = 0
    
    for i in my_list : 
        if i % 2 == 0 :
            continue
        elif i % 2 == 1 :
            sum += i

    print(f'#{test_case} {sum}')