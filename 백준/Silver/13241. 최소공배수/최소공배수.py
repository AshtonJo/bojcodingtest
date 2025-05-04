def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a

def lcm(a, b):
  res = a * b // gcd(a,b)
  return res

a, b = map(int, input().split())
print(lcm(a, b))