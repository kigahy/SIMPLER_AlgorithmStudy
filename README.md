# SSAFY 12기 알고리즘 스터디 [심플러(Simpler)] #
**심플러(Simpler)**, 어려운 코드도 간단히 처리하는 사람들

![이미지](./images/_66dbbd72-eb53-4f90-abbc-c1a6932679d9.jfif)
- 목표 : 스터디원 모두 SWEA 파이썬 B 취득
- 모임 : 매주 _요일 함께 저녁식사 후 1시간 30분 내외 *(월요일 or 목요일 추후 알림)*
- 장소 : 르하임스터디카페 부산명지점 4인 스터디룸 *(정기권 결제 예정)*
- 마감 : 모임 전날 저녁 8시 D1 매주 8문제, 각자 2개 발표

## 문제 ##

### 주차별 문제 목록 ###

<details>
<summary>1주차 SWEA D1 8문제</sumary>

2072. [홀수만 더하기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&)
2071. [평균값 구하기](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QRnJqA5cDFAUq&categoryId=AV5QRnJqA5cDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1)
2070. [큰 놈, 작은 놈, 같은 놈](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQ6qqA40DFAUq&categoryId=AV5QQ6qqA40DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1)
2068. [최대수 구하기](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQhbqA4QDFAUq&categoryId=AV5QQhbqA4QDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1)
2056. [연월일 달력](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QLkdKAz4DFAUq&categoryId=AV5QLkdKAz4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1)
2050. [알파벳을 숫자로 변환](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QLGxKAzQDFAUq&categoryId=AV5QLGxKAzQDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1)
2047. [신문 헤드라인](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QKsLaAy0DFAUq&categoryId=AV5QKsLaAy0DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1)
2046. [스탬프 찍기](https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QKdT6AyYDFAUq&categoryId=AV5QKdT6AyYDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=10&pageIndex=1)

</details>

### 플랫폼 ###
|플랫폼(링크)|태그|
|--|--|
|[백준](https://www.acmicpc.net)|BOJ|
|[엑스퍼트아카데미](https://swexpertacademy.com/main/main.do)|SWA|


## 스터디 규칙 ##

### 역할 ###
- 가현 : 팀장
- 진문 : 서기, 돈관리
- 혜령 : 문제 선정
- 원재 : 

### 프로그램 ###
- SWEA 메인, 백준도 함께
- 피그잼으로 시각화

### 문제 풀이 ###
- 매주 8문제, 각자 2개 발표
- 푼 문제 모두 GitHub에 업로드
- 모임 전날 저녁 8시 마감

### 발표 ###
- 매주 8문제 풀고 각자 2문제 발표
- 문제에서의 핵심 생각과 로직을 설명
- 돌아가며 인당 최대 15분

## 커밋 규칙 ##
### Repository clone ###
```
https://github.com/kimgahyeonn/algorithm.git
```

### Repository 폴더 구조 ###
```
{플랫폼}/[{문제번호}] {문제명}/{본인의 깃허브 이름}
```
- 예시 : `BOJ/[1234] 단어 길이 재기/kimgahyeonn`
- 플랫폼에 따라 없는 내용은 생략 가능

### 본인의 Branch 생성(?) ###

*7월 3주차 : 아직 매터모스트로 알린 후 Push. branch는 추후 설정*

```
git checkout -b {본인의 깃허브 이름}/{주차명}
```
- branch는 주차별로 생성
- 예시 : `git checkout -b gahyeonn/1week`

### push ###
```
git add .
git commit -m "{주차명} : {플랫폼}/[{문제번호}] {문제명}"
git push origin {생성한 브랜치}
```
- 예시 : git commit m "1week : BOJ[1234] 단어 길이 재기

### Pull Request 생성 ###
```
{본인의 깃허브 이름} : [{주차명}]
```
- 예시 : `kimgahyeonn : [1week]`
- 문제명, 시간복잡도, 시간 및 메모리 캡쳐, 플랫폼 기재
- 회의 마지막에 merge


## 참고자료 ##
- [SeongukBack님] (https://github.com/SeongukBaek/algoStudy)
- [CodeSquad-2023-BE-Study님] (https://github.com/CodeSquad-2023-BE-Study)