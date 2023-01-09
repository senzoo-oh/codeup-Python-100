num = int(input())
called_number = input().split()
data = []

for i in range(num):
  called_number[i] = int(called_number[i])

for i in range(num-1, -1, -1):
  print(called_number[i], end = ' ')

