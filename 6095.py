number_of_white = int(input())

arr = [[0 for i in range (20)] for j in range (20)]
arr.append(0)

for i in range(number_of_white):
  x, y = input().split()
  arr[int(x)][int(y)] = 1

for i in range (1, 20):
  for j in range (1, 20):
    print(arr[i][j], end=' ')
  print()
