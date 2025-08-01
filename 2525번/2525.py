hour, min = map(int, input().split())
time = int(input())

min += time

while not(min<60):
    min -= 60
    hour += 1
    
while not(hour<24):
    hour -= 24
    
print(hour, min)
    