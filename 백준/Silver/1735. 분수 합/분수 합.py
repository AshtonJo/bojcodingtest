# 1. 최대 공약수를 구한다
# 2. 분자와 분모를 각각 최대공약수로 나누면 기약분수형태의 답이나옴
def gcd(a, b):
  while b: 
    a, b = b, a % b
  return a # 1

a, b = map(int, input().split()) # 2 7
c, d = map(int, input().split()) # 3 5

top = a*d + b*c # 31
bottom = b*d # 35

gcd_ = gcd(top, bottom)
t = top // gcd_ # 31 // 1
b = bottom // gcd_ # 35 // 1
print(t , b) # 31 , 35
  