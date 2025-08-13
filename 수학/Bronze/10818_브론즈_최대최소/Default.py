#file = open('test.txt', 'r')
input_str = input() #file.readline()
num = int(input_str)

input_str = input() #file.readline()
array = list(map(int, input_str.split(' ')))

min = array[0]
max = array[0]

for x in array:
  if x < min:
    min =x
  if x > max:
    max = x

print(min,max)