while True:
  a, b, c = map(int, input().split())
  if a==0 and b==0 and c==0:
    break
    
  arr = sorted([a,b,c])
  if arr[2] >= arr[0] + arr[1]:
    print("Invalid")
  elif a == b == c:
    print("Equilateral")
  elif a==b or a==c or b==c:
    print("Isosceles")
  elif a != b and a != c and b != c:
    print("Scalene")
