def solution(numbers, target):
    count = DFS(numbers, target, 0)
    return count

def DFS(numbers, target, index):
    if index<len(numbers):
        pos_numbers = numbers[:]
        neg_numbers = numbers[:]
        neg_numbers[index] *= -1
        return DFS(pos_numbers, target, index+1) + DFS(neg_numbers, target, index+1)
    else:
        if sum(numbers) == target:
            return 1
        else:
            return 0