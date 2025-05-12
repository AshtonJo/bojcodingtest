# (x축가장 큰 값 - x축 가장 작은값) * (y축 가장 큰 값 - y축 가장 작은값)
n = int(input())
x_coords = []
y_coords = []

for _ in range(n):
  x, y = map(int, input().split())
  x_coords.append(x)
  y_coords.append(y)

if n == 1:
  print(0)
else:
  width = max(x_coords) - min(x_coords)
  height = max(y_coords) - min(y_coords)
  area = width * height
  print(area)