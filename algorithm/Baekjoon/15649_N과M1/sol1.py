'''
dfs + back tracking !!!! 손으로 그려보고 이해하기
'''


def dfs(i, N, M):
    # i값 = stack의 index 이므로, M과 동일해지면 append 하지말고 출력해줘    
    if i == M:
        print(' '.join(map(str, stack)))
    # idx가 아직 넘지 않았다면, 수열을 만들어줄거야
    else:
        for j in range(1, N+1):
            # 중복되지 않게 해야하니까! stack에 있으면 추가하지 말아야해
            if j not in stack:
                stack.append(j)
                dfs(i+1, N, M)
                # 백트래킹 구현! i+1에서 dfs 재귀 해주면 위의 if문에 걸리면서 출력되겠지
                # 그럼 다시 돌아와서 방금 넣어주고 출력되었던 stack의 마지막 값을 pop해주고,
                # 추가할 수 있는 다른 수들을 계속 반복해줘!
                stack.pop()


N, M = map(int, input().split())
stack = []  # 수열 받아줄 empty stack 만들기

dfs(0, N, M)  # dfs 호출 반복해주면서 수열 출력해주자!