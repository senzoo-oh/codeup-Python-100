day1, day2, day3 = map(int,input().split())

common_day = 1

while (common_day%day1!=0) or (common_day%day2!=0) or(common_day % day3 != 0):
  common_day += 1

print(common_day)
