from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0 # n 값을 넘지 않으면서 가장 큰 합을 저장할 함수

for combo in combinations(cards, 3):  
  current_sum = sum(combo)

  if current_sum <= m:
    max_sum = max(max_sum, current_sum)
    
print(max_sum)
  