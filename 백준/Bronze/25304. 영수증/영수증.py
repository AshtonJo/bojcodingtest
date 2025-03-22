X = int(input()) # 영수증 총 금액
N = int(input()) # 구매한 물건의 종류 수

total = 0 # 계산 총 금액

for _ in range(N):
    a, b = map(int, input().split())
    total += a * b

if total == X:
    print("Yes")
else:
    print("No")