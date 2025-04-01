word = input()
# 문자열 갯수에 따라 1씩더하기 문자열 1개면 +1 2개면 +2
time = 0
for w in word:
    if w in 'ABC':
        time += 3
    elif w in 'DEF':
        time += 4
    elif w in 'GHI':
        time += 5
    elif w in 'JKL':
        time += 6
    elif w in 'MNO':
        time += 7
    elif w in 'PQRS':
        time += 8
    elif w in 'TUV':
        time += 9
    elif w in 'WXYZ':
        time += 10
        
print(time)
    