a = [0,1,2]

number = int(input())

for i in range(3,number+1):
    a.append(a[i-1]+a[i-2])
    
print(a[number])