import sys
N = int(input())

line = sys.stdin.readline().strip()
a =list(map(int,line.split()))

# 10 -4 3 1 5 6 -35 12 21 -1

max_value = a[0]
current_sum = 0

for x in a:
    current_sum += x
    max_value = max(current_sum, max_value)
    if current_sum<0:
        current_sum = 0
        
print(max_value)