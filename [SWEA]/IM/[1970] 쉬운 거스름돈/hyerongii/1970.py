import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    total = int(input())

    # 돈 종류 : dict 만듬
    money = { 
        50000 : 0, 
        10000 : 0,
        5000 : 0,
        1000 : 0,
        500 : 0,
        100 : 0,
        50 : 0,
        10 : 0
        }
    
    for k, v in money.items():
        # 큰 금액부터 차례로 진행
        if (total//k) >= 1 :
            money[k] = total//k
            total = total - (k * money[k])

    print(f'#{test_case}')
    for v in money.values():
        print(v, end=" ")

    print()