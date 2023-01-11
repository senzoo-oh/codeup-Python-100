# 격자판의 크기
height, width = input().split()
height = int(height)
width = int(width)

board = []
for i in range(height):
  board.append([])
  for j in range(width):
    board[i].append(0)

# 막대의 개수 입력받기
num = int(input())

# 막대의 길이, 방향,좌표 입력받기
for i in range(num):
  length, direction, x, y = input().split()
  length = int(length)
  direction = int(direction)
  x = int(x)-1
  y = int(y)-1
  for j in range(length):
    if direction == 0:
      board[x][y] = 1
      y = y + 1
    else:
      board[x][y] = 1
      x = x + 1

# 격자판 출력
for i in range(height):
  for j in range(width):
    print(board[i][j], end = ' ')
  print()
