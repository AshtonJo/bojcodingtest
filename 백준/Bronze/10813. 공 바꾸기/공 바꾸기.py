N, M = map(int, input().split()) # [5, 4]
basket = [i+1 for i in range(N)] # [1, 2, 3, 4, 5]

for _ in range(M):
  i, j = map(int, input().split())
  basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

print(*basket)
  