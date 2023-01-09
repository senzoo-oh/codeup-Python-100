num = int(input())
number_called = input().split()

for i in range(num):
  number_called[i] = int(number_called[i])

d = []
for i in range(24):
  d.append(0)

for i in range(num):
  d[number_called[i]] += 1

for i in range(1,24):
  print(d[i], end=' ')
