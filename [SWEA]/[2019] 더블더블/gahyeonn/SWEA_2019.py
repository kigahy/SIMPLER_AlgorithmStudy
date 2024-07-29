num = int(input())

for i in range(num+1) :
    print((2**i), end=' ')


'''시행착오1
for i in range(1, num+1) :
    i += i
    print(i, end = ' ')
'''

'''시행착오2
val = 0
for i in range(1, num+1) :
    val = val + i
    print(val*2, end = ' ')
'''