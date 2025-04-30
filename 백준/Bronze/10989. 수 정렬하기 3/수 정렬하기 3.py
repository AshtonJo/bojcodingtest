import sys

input = sys.stdin.readline
n = int(input())
count = [0] * 10001 # 각 숫자의 등장 횟수를 기록할 배열

for i in range(n):
  num = int(input())
  count[num] += 1

for i in range(1, len(count)):
  if count[i]: # i라는 숫자가 한번이라도 나오면
    for _ in range(count[i]): # 그 숫자 카운트만큼 반복
      print(i) # count[5] == 2, count[2] == 2