T = int(input())

for test_case in range(1, T+1) :
    print(f'#{test_case}')
    inp = int(input())
    lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    mon = inp
    
    for i in range(len(lst)) :
        count = mon // lst[i]
        mon = mon - (count * lst[i])
        print(count, end = ' ')
    else :
        print('')
    


    
