while True:
  a,b = map(int, input().split())

  if a == b:
    break
  if a % b == 0:
    print("multiple")
  elif b % a == 0:
    print("factor")
  elif a%b != 0 and b%a != 0:
    print("neither")
  elif a == 0 and b == 0:
    break
  