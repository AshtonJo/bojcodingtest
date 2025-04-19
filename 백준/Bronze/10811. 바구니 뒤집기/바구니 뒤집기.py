# 바구니 개수 N, 반복 횟수 M
N, M = map(int, input().split())
numbers = list(range(1, N + 1))

for _ in range(M):
    i, j = map(int, input().split())
    numbers[i - 1:j] = reversed(numbers[i - 1:j])  # 슬라이싱으로 역순 삽입

print(*numbers)