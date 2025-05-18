# 큰 단위부터 나누면서 거슬러주니까 동전 개수가 최소되게 만들기

n = int(input())
# for _ in range(n):
#   money = int(input())
  
#   quarter = money // 25 # 124 // 25 = 4
#   money %= 25 # 남은돈 124 % 25 = 24

#   dime = money // 10 # 24 // 10 = 2
#   money %= 10 # 남은돈 24 % 10 = 4

#   nickel = money // 5 # 4 // 5 =  0
#   money %= 5 # 남은돈 4 % 5 = 4

#   penny = money # 남은돈 4
  
#   print(quarter, dime, nickel, penny)

for _ in range(n):
  money = int(input())
  
  for i in [25, 10, 5, 1]:
    print(money // i, end=' ')    
    money %= i
  print()
  