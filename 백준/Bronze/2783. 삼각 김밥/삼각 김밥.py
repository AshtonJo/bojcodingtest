X, Y = map(int, input().split()) # 세븐25 가격정보

N = int(input()) # 편의점 개수

# 1그램당 가격 =  X/Y 
# 1,000 그램 가격 = (X/Y) * 1000
min_price_per_gram = X / Y # 세븐일레븐 1그램당 가격

for _ in range(N):
  Xi, Yi = map(int, input().split()) # 편의점 가격 정보
  price_per_gram = Xi/Yi # 1그램당 가격
  min_price_per_gram = min(min_price_per_gram, price_per_gram)

print(f"{min_price_per_gram * 1000:.2f}")