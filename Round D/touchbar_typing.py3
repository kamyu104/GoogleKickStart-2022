# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round D - Problem C. Touchbar Typing
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76f44
#
# Time:  O(N * M), pass in PyPy3 but Python3
# Space: O(N * M)
#

def touchbar_typing():
    N = int(input())
    S = list(map(int, input().split()))
    M = int(input())
    K = list(map(int, input().split()))
    lookup = set(S)
    neis = [{}, {}]
    for idx, rng in enumerate([range(M), reversed(range(M))]):
        nei = neis[idx]
        prev = {}
        for i in rng:
            if K[i] not in lookup:
                continue
            nei[i] = {}
            for j, x in prev.items():
                nei[i][j] = x
            nei[i][K[i]-1] = i
            prev = nei[i]
    dp = {i:0 for i in range(M) if K[i] in lookup}
    for x in S:
        new_dp = {}
        for i, d in dp.items():
            for nei in [neis[0][i], neis[1][i]]:
                if x-1 not in nei:
                    continue
                j = nei[x-1]
                if j not in new_dp or new_dp[j] > d+abs(j-i):
                    new_dp[j] = d+abs(j-i)
        dp = new_dp
    return min(dp.values())

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, touchbar_typing()))
