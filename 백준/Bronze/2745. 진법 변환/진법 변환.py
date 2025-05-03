# 0~Z 까지 포함된 문자열을 활용한다. 이 문자열의 index가 곧 값이 됨을 이용
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = input().split() # ["ZZZZZ", "36"]
res = 0

for i, char in enumerate(n[::-1]): # 0 Z
    # 자리값 x (진법의 자리수 제곱) => 35 * 36의 4승 + ...
    # res는 B진법수를 10진법으로 바꾸는 계산식 (Z * 36) ** 4 + ... 
    res += num_list.index(char) * (int(b) ** i)
    
print(res)