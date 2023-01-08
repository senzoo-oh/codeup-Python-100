number = int(input())
sum = 0
c = 1

while True:
  sum += c
  c += 1
  if sum >= number:
    break

print(sum)