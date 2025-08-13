file = open("test.txt",'r')

input_str = file.readline()
N, S = map(int, input_str.split(" "))
input_str = file.readline()
A_list = list(map(int, input_str.split(" ")))

def GCC(x, y):
  while y:
    x, y = y, x%y
  return x

for i in range(0, N):
  A_list[i] = A_list[i] - S
  if A_list[i] <0:
    A_list[i] = int(A_list[i]*-1)

result = A_list[0]
for x in A_list:
  result = GCC(result,x)
print(result)