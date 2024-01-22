#file = open('test.txt', 'r')

input_str = input()  #file.readline()
N, K = map(int, input_str.split(' '))

num_list = [0]

for x in range(1, N + 1):
  if N % x == 0:
    num_list.append(x)
if len(num_list) <= K:
  print(0)
else:
  print(num_list[K])
