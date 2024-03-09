a, b = map(int, input().split(" "))

# a_value, b_value, a_count, b_count

sum_post = 0
for i in range(1, 10001):
  sum_post += i
  if sum_post >= a:
    sum_past = sum_post-i
    a_value = i
    a_count = a - sum_past - 1
    break

sum_post = sum_past 
for i in range(a_value, 10001):
  sum_post += i
  if sum_post >= b:
    b_value = i
    b_count = sum_post - b
    break

sum = 0
for i in range(a_value, b_value+1):
  for j in range(i):
    sum += i

for i in range(a_count):
  sum = sum - a_value

for i in range(b_count):
  sum = sum - b_value

print(sum)