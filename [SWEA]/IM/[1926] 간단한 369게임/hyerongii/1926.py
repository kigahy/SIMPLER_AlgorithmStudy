# 369게임
# string으로 받고 369있으면 카운트 그 개수만큼 -으로 프린트 

N = int(input())
num_lst = list(map(str, range(1, N+1)))

for num in num_lst:
    count = 0

    # 36이면 3,6 으로 나누어 생각
    for n in num:
        if n == '3' or n == '6' or n == '9':
            count += 1
    
    if count > 0:
        print("-" * count, end=" ")
    else:
        print(num, end = " ")