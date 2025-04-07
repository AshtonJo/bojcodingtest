def pyramid(floor):
  for i in range(1, floor+1):
    space = " " * (floor - i)
    star = "*" * i
    res = space + star
    print(res)

N = int(input())
pyramid(N)
