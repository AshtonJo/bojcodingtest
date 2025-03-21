# 1. N,X 입력받는다
# 2. 수열 A를 입력받는다
# 3. X보다 작은 숫자만 출력한다

result = [] # X보다 작은 숫자를 리스트에 추가
# N은 수열길이 X는 기준값. 공백기준, 문자열을 입력받아 리스트로 변경
N, X = map(int, input().split())
# map은 리스트의 모든 요소를 정수로 변환
# list는 변환된 값을 다시 리스트로 저장
# 즉 정수로 변환된 모든 요소의 값을 리스트로 저장
A = list(map(int, input().split()))

# num은 리스트A 안에 있는 수, num < X 조건을 만족하는 값만 리스트에 저장
for num in A:
  if num < X:
    result.append(num)
 # 여기까지오면 [1, 4, 2, 3] 으로 나옴

# 리스트를 없애고 공백으로 구분해서 출력
# join() 함수는 리스트이 요소들을 하나의 문자열로 합쳐준다.
print(" ".join(map(str, result)))