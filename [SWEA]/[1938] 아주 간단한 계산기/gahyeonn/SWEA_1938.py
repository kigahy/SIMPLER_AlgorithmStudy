lst = list(map(int, input().split()))
lst.sort() # 오름차순으로 정렬
i = 0

print(lst[i] + lst[i+1])

print(lst[i+1] - lst[i]) # 더 큰 값에서 작은 값 -

print(lst[i] * lst[i + 1])

print(lst[i+1] // lst[i]) # 더 큰 값에서 작은 값 //