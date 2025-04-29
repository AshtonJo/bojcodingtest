n = int(input())
arr = []
for _ in range(n):
  xi,yi = map(int, input().split())
  arr.append((xi,yi))
  
arr.sort(key=lambda x:(x[1],x[0]))
for xi,yi in arr:
  print(xi,yi)

