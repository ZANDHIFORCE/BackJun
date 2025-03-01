number = int(input())
first = 1
second = 2
for i in range(3,number+1):
    first , second = second%15746, (first + second)%15746
    
if number ==1:
    second=1
elif number ==2:
    second=2
    
print(second%15746)