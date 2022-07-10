# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round D - Problem C. Touchbar Typing
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76f44
#
# Time:  O(M * MAX_K + N * M), pass in PyPy3 but Python3
# Space: O(M * MAX_K)
#

def touchbar_typing():
    N = int(input())
    S = list(map(int, input().split()))
    M = int(input())
    K = list(map(int, input().split()))
    MAX_K = max(K)
    prev = [[-1]*MAX_K for _ in range(M+1)]
    for i in range(M):
        for j in range(MAX_K):
            prev[i+1][j] = prev[i][j]
        prev[i+1][K[i]-1] = i
    nxt = [[-1]*MAX_K for _ in range(M+1)]
    for i in reversed(range(M)):
        for j in range(MAX_K):
            nxt[i][j] = nxt[i+1][j]
        nxt[i][K[i]-1] = i
    dp = [0]*M
    INF = N*(M-1)+1
    for x in S:
        new_dp = [INF]*len(dp)
        for i, d in enumerate(dp):
            if d == INF:
                continue
            for j in [prev[i+1][x-1], nxt[i][x-1]]:
                if j != -1:
                    new_dp[j] = min(new_dp[j], d+abs(j-i))
        dp = new_dp
    return min(dp)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, touchbar_typing()))
