T = int(input())

for test_case in range(1, T + 1):

    values = list(map(int, input().split()))
    value = max(values)
    print(f'#{test_case} {value}')
