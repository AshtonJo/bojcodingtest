submit = [] # 제출한 사람 번호

for _ in range(28):
  n = int(input())
  submit.append(n) # [3,1,4, ...]
  
# 1~30중 제출 안한번호
# 30번 반복 돌리면서 제출한 사람배열에 없는 숫자를 제출 안한 사람배열에 삽입
notsubmit = [] # 제출 안한 사람번호
for i in range(1, 31):
  if i not in submit:
    notsubmit.append(i) # [2, 8]

res = sorted(notsubmit)
print(res[0])
print(res[1])