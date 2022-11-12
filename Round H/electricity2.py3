# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round H - Problem C. Eelectricity
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb1b6/0000000000c47c8e
#
# Time:  O(N)
# Space: O(N)
#

def iter_dfs(adj, dp, u):
    stk = [(1, u)]
    while stk:
        step, u = stk.pop()
        if step == 1:
            if dp[u]:
                continue
            stk.append((2, u))
            for v in adj[u]:
                stk.append((1, v))
        elif step == 2:
            dp[u] += 1+sum(dp[v] for v in adj[u])

def electricity():
    N = int(input())
    A = list(map(int, input().split()))
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        X, Y = map(int, input().split())
        X -= 1
        Y -= 1
        if A[X] == A[Y]:
            continue
        if A[X] < A[Y]:
            X, Y = Y, X
        adj[X].append(Y)
    dp = [0]*len(adj)
    for u in range(N):
        iter_dfs(adj, dp, u)
    return max(dp)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, electricity()))
