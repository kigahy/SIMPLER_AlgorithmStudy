T = int(input())

for test_case in range(1, T + 1):
    a, b = map(int, input().split()) # 두 값 map으로 int 형변환

    c = a // b
    d = a % b
    
    print(f'#{test_case} {c} {d}')