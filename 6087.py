# number = int(input())

# for i in range(number+1):
#   if (i % 3 != 0):
#     print("%d" % i, end = " ")
#   else:
#     continue

n = int(input())

for i in range(1, n+1):
  if i%3==0 :
    continue
  print(i, end=' ')