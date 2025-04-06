# 테스트 케이스 수 입력
T = int(input())

for i in range(1, T + 1):
    A, B = map(int, input().split())
    print(f"Case #{i}: {A + B}")