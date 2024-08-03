# [2056] 연월일 달력 #

연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
 
해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면 "YYYY/MM/DD"형식으로 출력하고, 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.


연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며 일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
 

※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)


**[입력]**

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다. 다음 줄부터 각 테스트 케이스가 주어진다.


**[출력]**

테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다. (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

```
T = int(input())

def true_prin() : # 0 포함한 날짜값 출력
     print(f'#{test_case} {year:04}/{month:02}/{day:02}')

def false_prin() : # 틀린 날짜일 때 -1 출력
    print(f'#{test_case} -1')

for test_case in range(1, T + 1):
    input_day = input()
    
    years = input_day[:4] # 리스트 앞에서 4개는 연도
    months = input_day[4:6] # 리스트 4부터 5까지 달
    days = input_day[6:8] # 리스트 6부터 8까지 일

    year = int(years) # 문자열을 정수형으로 형변환
    month = int(months)
    day = int(days)

        
    if month in [1, 3, 5, 7, 8, 10, 12] : # 월 검사
        if day < 1 or day > 31 : # 일 검사
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
```
- 개인적으로 **가장 어려웠던 문제**로, 다른 팀원의 코드가 무척이나 궁금해지는 문제
- 올바른 날짜와 틀린 날짜의 값을 출력할 함수를 `true_prin()`과 `false_prin()`으로 각각 선언
- `true_prin()`을 출력할 때, 07월 아닌 0을 제외하고 7월만 반환하는 문제점으로 `{month:02}` 추가
- 날짜 문자열을 리스트로 하여 각 years, months, days 변수에 리스트의 자릿수로 구분
- 이후 if문 통하여 ~~노가다~~ 