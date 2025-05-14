# 삼각형: 작은 두 변의 길이의 합이 제일 긴변의 길이보다 커야함
arr = sorted(list(map(int, input().split())))
if arr[0] + arr[1] > arr[2]:
  print(sum(arr))
else:
  # a+b + a+b-1
  # [1,2,3] = 1 + 2 + (1 + 2 + 2)
  print(arr[0] + arr[1] + (arr[0] + arr[1] - 1))
  