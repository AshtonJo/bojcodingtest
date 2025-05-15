def binary_search(arr, target):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2
    
    if arr[mid] == target:
      return 1
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  
  return 0

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
targets = list(map(int, input().split()))

for t in targets:
  print(binary_search(a, t))
    
  
