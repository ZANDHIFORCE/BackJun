#file = open("test.txt", "r")

total = 0
max = 0

for _ in range(10):
  input_str = input() #file.readline()
  pout, pin = map(int, input_str.split(" "))
  total = total - pout + pin
  if total>max:
    max = total

print(max)