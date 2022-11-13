# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round H - Problem C. Eelectricity
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb1b6/0000000000c47c8e
#
# Time:  O(NlogN)
# Space: O(N)
#

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
        if A[X] > A[Y]:
            X, Y = Y, X
        adj[X].append(Y)
    idx = list(range(N))
    idx.sort(key=lambda x: A[x])
    dp = [1]*N
    for u in idx:
        for v in adj[u]:
            dp[v] += dp[u]
    return max(dp)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, electricity()))
