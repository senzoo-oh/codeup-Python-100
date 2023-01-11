# 바둑판 생성

board = []
for i in range(20):
  board.append([])
  for j in range(20):
    board[i].append(0)

# 정수 1, 0의 입력을 받는다.
for i in range(19):
  a = input().split()
  for j in range(19):
    board[i+1][j+1] = int(a[j])

# 뒤집을 횟수 입력 받기
num = int(input())

# 뒤집을 좌표 입력 받기
for i in range(num):
  x, y = input().split()
  x = int(x)
  y = int(y)
  for j in range(1,20):
    if board[j][y] == 0:
        board[j][y] = 1
    else:
        board[j][y] = 0
    if board[x][j] == 0:
        board[x][j] = 1
    else:
        board[x][j] = 0
        
for i in range(1,20):
  for j in range(1,20):
    print(board[i][j], end=" ")
  print()
