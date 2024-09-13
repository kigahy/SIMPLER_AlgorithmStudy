'''
배열이 주어지고 배열의 원소들에 -1을 곱하면서
target이 되는 조합을 찾으면 되겠다 생각하고 문제에 접근했습니다.
numbers = [1, 1, 1, 1, 1]
target = 3
combination
[-1, 1, 1, 1, 1]
[1, -1, 1, 1, 1]
[1, 1, -1, 1, 1]
[1, 1, 1, -1, 1]
[1, 1, 1, 1, -1]
return = 5
'''


answer = 0


def solution(numbers, target):
    target_number(0, numbers, target)
    return answer


def target_number(num, numbers, target):
    global answer

    if num == len(numbers):  # 인덱스가 배열의 길이과 같아지고 리스트의 합이 target과 같으면
        if sum(numbers) == target:
            answer += 1     # answer + 1
        return
    # 재귀로 돌아가다 리스트의 합이 target 보다 작으면 return
    # (-1이나 1이 곱해져 재귀로 돌아가면 리스트의 합이 작거나 같아질 경우 밖에 없기 때문에)
    if sum(numbers) < target:
        return

    for i in [-1, 1]:   # -1과 1을 번갈아 곱해주면서 재귀로 target을 찾아간다.
        numbers[num] *= i   # -1이나 1을 numbers 해당 인덱스에 곱해주고
        target_number(num + 1, numbers, target)  # 다음 인덱스를 넘겨주며 재귀
        numbers[num] *= i   # -1이나 1을 다시 곱해줘 원상복구