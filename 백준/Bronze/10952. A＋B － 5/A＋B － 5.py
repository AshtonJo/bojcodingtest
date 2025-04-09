# 0 0 이 들어오면 입력 종료

while True:
  A, B = map(int, input().split())
  
  if A == 0 and B == 0:
    break
    
  print(A + B)
  