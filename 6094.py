num = int(input())
k = input().split()
memory = int()

for i in range(num):
  k[i] = int(k[i])

k.sort()
print(k[0])