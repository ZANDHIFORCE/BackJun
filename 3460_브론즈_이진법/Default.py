file = open("test.txt",'r')

input_str = file.readline()
N, S = map(int, input_str.split(" "))
input_str = file.readline()
A_list = list(map(int, input_str.split(" ")))

for i in range(0, N):
  A_list[i] = A_list[i] - S
  if A_list[i] <0:
    A_list[i] = int(A_list[i]*-1)

min = A_list[0]
for x in A_list:
  if x < min:
    min = x

check = True
for i in range(min,-1,0):
  for x in A_list:
    if x % i != 0:
      check = False
      break
  if check is True:
    print(i)
    break