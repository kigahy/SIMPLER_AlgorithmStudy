# 애너그램 찾기

- 애너그램 : 문자의 순서나 대소에 관계없이 똑같은 문자들로 구성된 두 문자열.
- 두 문자열이 같은지 판단
- 알고리즘은 sorted함수 채택
- O(n log n)

```
def is_anagram(s1, s2) :
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    # 공백을 모두 제거하고 소문자로 통일

    if sorted(s1) == sorted(s2) :
        return True
    else :
        return False
    # 문자열을 정렬하여 비교
```


# 팰린드롬 찾기

- 거꾸로 읽어도 똑같은 단어
- mom, Hannah 등
- 문자열을 복사해 순서를 뒤집은 다음 원래 문자열과 비교하여 일치하면 팰린드롬인 것
- 요소 전체를 하나씩 비교해야 하므로 O(n)

```
print("blackswan"[::-1])
```
결과 : `nawskalb`
```
def is_palindrome(s1):
    if is s1.lower() == s1[::-1].lower():
    # 내장 함수 lower로 문자를 모두 소문자로 변환
        return True
    # 두 문자열이 일치하면 팰린드롬이므로 True 반환
    else :
        return False
```

# 마지막 숫자

- 문자열의 가장 오른쪽에 있는 숫자를 찾는 문제
- **리스트 축약** : 원래의 iterable 리스트에서 새로운 리스트로 만드는 파이썬 문법 활용
- 모든 글자 순회하므로 O(n)

```
new_list = [expression(i) for i in iterable if filter(i)]
```
- iterable은 새로운 리스트를 만들기 위한 재료
- expression(i)는 iterable의 각 요소를 저장할 변수
- filter(i)에 if조건문 가능

` print([c for c in "selftaught"])`
결과: `['s', 'e', 'l', 'f', ... , 't']`

### 마지막 숫자 1단계
```
s = "Buy 1 get 2 free"
nl = [c for c in s if c.isdigit()] #문자열에서 숫자만 남기는 함수
print(nl)
```
결과: `['1', '2']`

- 새로운 리스트에서 마지막 숫자를 찾는 가장 간단한 방법은 **음수 인덱스**

```
s = "Buy 1 get 2 free"
nl = [c for c in s if c.isdigit()][-1]
print(nl)
```
결과: `2`

# 시저의 암호

- 암호 : 암호화나 복호화에 사용되는 알고리즘
- abc -> def 처럼 모든 문자를 특정 숫자만큼 이동시킴
---
- 시간과 관련한 프로그램을 만들 때는 대부분 나머지 연산을 사용
- 9시에 출발하여 8시간이 걸리는 시간 함수 `17 % 12` 결과 `5` 
---
```
import string

def cipher(a_string, key):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    # string 모듈로 대문자, 소문자, 각각의 알파벳 문자열을 하나씩 생성

    encrypt = ''
    # 빈 문자열 생성하여 추후 암호회된 문자 할당

    for c in a_string: # 각 문자 순회하며 c에 저장

        if c in uppercase:
            new = (uppercase.index(c) + key) % 26
            encrypt += uppercase[new]
        else c in lowercase:
            new = (lowercase.index(c) + key) % 26
            encrypt += lowercase[new]
        else:
            encrypt += c

        # 해당 대문자라면 대문자 문자열에서 찾고, 그 인덱스에 알파벳의 개수인 26으로 나눈 나머지로 key를 더하여 암호화된 문자 얻음

    return encrypt
```
- 나머지 연산은 문자열의 인덱스가 정해진 숫자(ex. 알파벳의 경우 25)를 얼마나 넘어가는지 구하는 것