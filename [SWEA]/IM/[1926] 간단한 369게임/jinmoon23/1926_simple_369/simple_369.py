
def simple_369_game(N):
    list_of_369 = ['33','36','39','63','66','69','93','96','99'] # 2개의 3 또ㄴ 6 또는 9를 식별할 경우를 대비하기 위한 list
    str_number_list = list(map(str,range(1,N+1)))

    for index,string in enumerate(str_number_list): # enumerate 메서드로 인덱스와 값에 접근
        if string in list_of_369:
            str_number_list[index] = '--' # 박수 두 번을 출력해야 하는 경우를 먼저 확인
            continue # 아래 코드를 실행시키지 않도록 continue로 반복문 제어
        if '3' in string or '6' in string or '9' in string:
            str_number_list[index] = '-'

    return ' '.join(str_number_list)



N = int(input())
print(simple_369_game(N))