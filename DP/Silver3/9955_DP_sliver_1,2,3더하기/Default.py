# 4
# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1

##

import sys

a = []
a.append([0,0,0])
a.append([1,0,0]) #1
a.append([1,1,0]) #2
a.append([1,2,0]) #3
a.append([1,4,2]) #4

input_number = int(input())
input_data = []
max = 0
for i in range(input_number):
    number = int(input())
    max = number if max<number else max
    input_data.append(number)
    

a=[0,1,2,4]

if max>3:
    for i in range(4,max+1):
        a.append(a[i-1]+a[i-2]+a[i-3]) #sum(a[i-3:i])

for x in input_data:
    print(a[x])
    




    
