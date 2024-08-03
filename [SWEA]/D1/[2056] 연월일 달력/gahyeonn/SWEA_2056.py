T = int(input())

def true_prin() : 
     print(f'#{test_case} {year:04}/{month:02}/{day:02}')

def false_prin() :
    print(f'#{test_case} -1')

for test_case in range(1, T + 1):
    input_day = input()
    
    years = input_day[:4]
    months = input_day[4:6]
    days = input_day[6:8]

    year = int(years)
    month = int(months)
    day = int(days)

        
    if month in [1, 3, 5, 7, 8, 10, 12] :
        if day < 1 or day > 31 :
            false_prin()
        else : 
                true_prin()
    elif month in [4, 6, 9, 11] :
        if day < 1 or day > 30 :
            false_prin()
        else : 
            true_prin()
    elif month == 2 :
        if day < 1 or day > 28 :
            false_prin()
        else : 
            true_prin()
    elif month < 1 or month > 12 :
        false_prin()
        

    

