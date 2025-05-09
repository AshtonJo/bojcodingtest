# 규칙찾다보니 x,y좌표가 혼자 다르면 그게 출력값임을 발견
# 좌표 3개를 입력 받고 x좌표와 y좌표를 
# 따로 리스트에 저장한 뒤에 혼자서 다른 x좌표와 y좌표를 출력
x_arr = []
y_arr = []

for _ in range(3):
  x, y = map(int, input().split())
  x_arr.append(x)
  y_arr.append(y)

for i in range(3):
  if x_arr.count(x_arr[i]) == 1:
    x4 = x_arr[i]
  elif y_arr.count(y_arr[i]) == 1:
    y4 = y_arr[i]

print(x4,y4)
