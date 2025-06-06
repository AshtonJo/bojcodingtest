T = int(input())
    
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return a * b / gcd(a, b)
     
for _ in range(T):
    A, B = map(int, input().split())
    res = lcm(A, B)
    print(int(res))