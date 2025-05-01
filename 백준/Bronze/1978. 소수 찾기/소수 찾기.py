# 소수: 1과 자기자신으로만 나누어 떨어지는 수

n = int(input())
numbers = list(map(int, input().split()))[:n]

def is_prime(x):
  if x < 2:
    return False
  for i in range(2, int(x ** 0.5) + 1):
    if x % i == 0:
      return False
  return True

count = 0

for num in numbers:
  if is_prime(num): # 소수면 count 1씩 증가
    count += 1
    
print(count)

    