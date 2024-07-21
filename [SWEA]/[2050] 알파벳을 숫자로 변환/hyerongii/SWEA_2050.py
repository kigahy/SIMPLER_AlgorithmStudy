# import sys
# sys.stdin = open("input.txt", "r")

'''
알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.

[제약 사항]
문자열의 최대 길이는 200이다.

[입력]
알파벳으로 이루어진 문자열이 주어진다.

[출력]
각 알파벳을 숫자로 변환한 결과값을 빈 칸을 두고 출력한다.
'''
T = input() #['ABCDEFG...']
num_list = []

# str 하나하나씩 나누기
for alpa in T: 
    # 대문자 숫자 65로 시작하게 변환: ord 
    # int -> str 로 변환 -> list에 추가
    num_list.append(str(ord(alpa)-65+1))
# join 사용하여 빈칸두고 출력
print(' '.join(num_list))


