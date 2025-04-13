N, M = map(int, input().split()) # [5, 4]
basket = [0] * N # 바구니 수 [0, 0, 0, 0, 0]
for _ in range(M):
  i, j, k = map(int, input().split())
  for index in range(i-1, j):
    basket[index] = k # [3,3]

print(" ".join(map(str,basket)))

# " ".join(map(str,basket))
# [1, 2] => ["1", "2", "1 2"]
