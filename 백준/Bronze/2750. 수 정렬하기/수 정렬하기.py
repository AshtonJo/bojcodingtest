N = int(input())  
arr = []

for i in range(N):
  num = int(input())
  arr.append(num)

# [5,2,3,4,1]
arr.sort()
# [1,2,3,4,5]

for num in arr:
  print(num)


