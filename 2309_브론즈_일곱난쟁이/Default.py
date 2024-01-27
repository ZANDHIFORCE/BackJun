#file = open("test.txt", "r")

ppl = []
total = 0

for _ in range(9):
  input_str = input() #file.readline()
  num = int(input_str)
  total += num
  ppl.append(num)

ppl.sort()

try: 
  for i in range(8):
    for j in range(i+1, 9):
      if (total-ppl[i]-ppl[j])==100:
        first, second = ppl[i], ppl[j]
        ppl.remove(first)
        ppl.remove(second)
        raise StopIteration

except StopIteration:
  for x in ppl:
    print(x)