#1 1 1 2 2 3 "4" 5 7 9 "12" 16 21
#a[i] = a[i-1] + a[i-5] asd

a = [0,1,1,1,2]

repeat_num = int(input())
input_list = []
max = 0
for i in range(repeat_num):
    element = int(input())
    max = element if max < element else max
    input_list.append(element)
    
for i in range(5,max+1):
    a.append(a[i-1]+a[i-5])
    
for x in input_list:
    print(a[x])

