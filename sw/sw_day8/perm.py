'''
순열 매우 중요해~ 구조 외우자~
'''
def perm(i):
    # 종료 조건
    if i == len(p):
        print(p)
    else: # 아직 다 못돌았으면
        for j in range(i, len(p)): # 그 다음순서부터 돌건데
            p[i], p[j] = p[j], p[i] # 순서를 바꿔 (swap)
            perm(i + 1) # 그담에 재귀 호출
            p[i], p[j] = p[j], p[i] # 다시 원래대로 바꿔줘

p = [1, 2, 3]

perm(0)