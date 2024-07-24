# 하이브리드 정렬 알고리즘

문제를 해결하는 데 두 개 이상의 알고리즘을 결합한 알고리즘

## 팀 정렬
- 삽입 정렬과 병합 정렬을 결합하여 만듦
- 직접 작성하기보다 파이썬에 내장된 정렬 알고리즘을 사용할 것을 권장


## sorted 함수

```
a_list = [1, 8, 10, 33 ,4, 103]
print(sorted(a_list_))
```
결과: `[1, 4, 8, 10, 33, 103]`

```
a_list = ["onehundred", five", "seventy", "two"]
print(sorted(a_list, key=len))
```
결과: `['two', 'five', 'seventy', 'onehundred']

- sort 함수는 리스트에서만 사용하며, 새로운 리스트를 반환하는 것이 아닌 기존 리스트 수정