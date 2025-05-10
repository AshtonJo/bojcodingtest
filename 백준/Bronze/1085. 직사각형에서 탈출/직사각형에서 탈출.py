x,y,w,h = map(int, input().split())
min_val = min(x, y, w-x, h-y)
print(min_val)
