# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round C - Problem D. Palindromic Deletions
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20d16
#
# Time:  O(N^3), pass in PyPy3 but Python3
# Space: O(N^2)
#

from functools import reduce

def inv_nCr(n, k):
    if not (0 <= k <= n):
        return 0
    while len(INV) <= n:
        FACT.append(FACT[-1]*len(INV) % MOD)
        INV.append(INV[MOD%len(INV)]*(MOD-MOD//len(INV)) % MOD)
        INV_FACT.append(INV_FACT[-1]*INV[-1] % MOD)
    return (INV_FACT[n]*FACT[n-k] % MOD) * FACT[k] % MOD

def palindromic_deletions():
    N = int(input())
    S = input()
    result = 1
    dp = [[[0]*N for _ in range(N)] for _ in range(2)]
    for i in range(N):
        dp[1][i][i] = 1
    for i in range(N):
        for j in range(i+1, N):
            dp[0][i][j] = int(S[i] == S[j])
    for l in range(1, N):
        total = reduce(lambda x, y: (x+y)%MOD, (dp[l%2][i][j] for i in range(N) for j in range(i, N)))
        result = (result+total*inv_nCr(N, l))%MOD
        for i in reversed(range(N-1)):
            for j in range(i, N):
                dp[l%2][i][j] = (dp[l%2][i][j]+dp[l%2][i+1][j])%MOD
        for i in reversed(range(N)):
            for j in range(i+1, N):
                dp[l%2][i][j] = (dp[l%2][i][j]+dp[l%2][i][j-1])%MOD
        dp[l%2] = [[dp[l%2][i+1][j-1] if i+1 <= j-1 and S[i] == S[j] else 0 for j in range(N)] for i in range(N)]
    return result

MOD = 10**9+7
FACT, INV, INV_FACT = [[1]*2 for _ in range(3)]
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, palindromic_deletions()))
