n, k = map(int, input().split())
arr = []
for i in range(1, n+1):
    if n%i == 0:
       arr.append(i) # 1, 2, 3, 6
    
if len(arr) < k:
    print(0)
else:
    print(arr[k-1])
 