# 구글 검색을 통하여 풂

s = '#'
p = '+'

for i in range(5) : # 가로 5번 반복
    for j in range(5) : # 세로 5번 반복

        if i == j : # 행과 열 값 같으면 # 출력
            print(s, end='')
        else : # 행과 열 값 다르면 + 출력
            print(p, end='')
            
    print('')
