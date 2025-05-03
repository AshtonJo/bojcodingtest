# 1~n-1 까지 검사하면서 분해합이 n과 같은 i가 있으면 출력하고 종료
# i의 분해합을 계산하는 함수를 만들자
# 그런 수가 없으면 0을 출력
# 분해합이 N이 되는 가장 작은 수를 찾는 것이 목표
n = int(input()) # 216
    
def digit_sum(x): # x = 198
    sum_ = 0
    for i in str(x): # x = 198 => str(198)=> '1', '9', '8'
        sum_ = sum_ + int(i) # sum_ = 1 + 9 + 8
    return x + sum_ # 198 + (1 + 9 + 8) => 216
     
result = 0
for i in range(1, n): # 1~215
    if digit_sum(i) == n: # digit_sum(198) == 216 => True
        result = i # result = 198
        break
        
print(result)