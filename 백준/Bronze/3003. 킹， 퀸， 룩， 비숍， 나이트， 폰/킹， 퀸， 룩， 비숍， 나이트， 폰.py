# 정상적인 원래 체스 피스 개수 정의
# 결과값 담을 리스트 생성
# 입력값(현재 보유한 피스 개수)받기
# 정상적인 개수에서 입력받은 개수를 빼서 결과리스트 생성
# 결과 출력하기

origin_pcs = [1, 1, 2, 2, 2, 8]
result_arr = []
possessed_pcs = list(map(int,input().split()))

result_arr = [origin_pcs[i] - possessed_pcs[i] for i in range(6)]
result = map(str, result_arr) # ["1", "0", "0", "0", "0", "1"]
result = " ".join(result)

print(result)