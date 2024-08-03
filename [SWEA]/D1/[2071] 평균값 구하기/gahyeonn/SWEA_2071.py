T = int(input())
for test_case in range(1, T + 1):
    val = input().split(' ')
    int_val = list(map(int, val))
    sum = 0
    ave = 0

    for num in int_val :
        sum += num
        ave = sum / len(int_val)

    print(f'#{test_case} {round(ave)}')

    