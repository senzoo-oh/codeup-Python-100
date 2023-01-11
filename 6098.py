# 10 * 10의 상자 만들기.
mirror_box = []
for i in range(10):
  mirror_box.append([])
  for j in range(10):
    mirror_box[i].append(0)

# 미로상자의 구조와 먹이의 위치 입력받기.
for i in range(10):
  a = input().split()
  for j in range(10):
    mirror_box[i][j] = int(a[j])

# # 개미 이동시키기. (무한루프 발생)
# x = int(1)
# y = int(1)
# while mirror_box[x][y] != 2:
#   if mirror_box[x][y+1] == 0:
#     mirror_box[x][y] = 9
#     y = y + 1
#   elif (mirror_box[x+1][y] == 1) and (mirror_box[x][y+1] == 1):
#     break
#   elif mirror_box[x][y+1] == 1:
#     mirror_box[x][y] = 9
#     x = x + 1

# mirror_box[x][y] = 9

# 개미 이동시키기 - 1.
x = int(1)
y = int(1)
while mirror_box[x][y] != 2:
  if (mirror_box[x+1][y] == 1) and (mirror_box[x][y+1] == 1):
    break
  elif mirror_box[x][y+1] != 1:
    mirror_box[x][y] = 9
    y = y + 1
  else:
    mirror_box[x][y] = 9
    x = x + 1

mirror_box[x][y] = 9

# 개미가 지나간 경로 출력하기.
for i in range(10):
  for j in range(10):
    print(mirror_box[i][j],end = ' ')
  print()