x = int(input())
recur = int(input())

total = 0
for _ in range(recur):
    value, num = map(int, input().split())
    total += value*num
    
print("Yes" if x == total else "No")