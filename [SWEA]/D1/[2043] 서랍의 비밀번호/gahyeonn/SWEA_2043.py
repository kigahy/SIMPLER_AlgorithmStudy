lst = list(map(int, input().split()))
lst.sort()

i = 0
val = lst[i+1] - lst[i] + 1

print(val)    