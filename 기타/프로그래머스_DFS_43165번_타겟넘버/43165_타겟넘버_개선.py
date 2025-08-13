def solution(numbers, target):
    def DFS(index,current_sum):
        if index<len(numbers):
            return DFS(index+1, current_sum+numbers[index]) + DFS(index+1, current_sum-numbers[index])
        else:
            if current_sum == target:
                return 1
            else:
                return 0
    count = DFS(0, 0)
    return count