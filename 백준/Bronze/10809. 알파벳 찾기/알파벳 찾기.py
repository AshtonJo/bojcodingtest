positions = [-1] * 26

S = input()

# ord('a') = 97
# 시작 문자 - 아스키코드변환('a') = 알파벳의 인덱스(0부터)
for i in range(len(S)):  
  index = ord(S[i]) - ord('a')
  if positions[index] == -1:
    positions[index] = i

# print(positions)
res = " ".join(map(str, positions))
print(res)
    