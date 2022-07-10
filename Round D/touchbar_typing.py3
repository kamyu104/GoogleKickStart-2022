# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round D - Problem C. Touchbar Typing
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76f44
#
# Time:  O(N * M), pass in PyPy3 but Python3
# Space: O(N * M)
#

from collections import defaultdict

def touchbar_typing():
    N = int(input())
    S = list(map(int, input().split()))
    M = int(input())
    K = list(map(int, input().split()))
    lookup = set(S)
    left = defaultdict(dict)
    prev = {}
    for i in range(M):
        if K[i] not in lookup:
            continue
        for j, x in prev.items():
            left[i+1][j] = x
        left[i+1][K[i]-1] = i
        prev = left[i+1]
    right = defaultdict(dict)
    prev = {}
    for i in reversed(range(M)):
        if K[i] not in lookup:
            continue
        for j, x in prev.items():
            right[i][j] = x
        right[i][K[i]-1] = i
        prev = right[i]
    dp = {i:0 for i in range(M)}
    for x in S:
        new_dp = defaultdict(lambda:N*(M-1)+1)
        for i, d in dp.items():
            for nei in [left[i+1], right[i]]:
                if x-1 not in nei:
                    continue
                j = nei[x-1]
                new_dp[j] = min(new_dp[j], d+abs(j-i))
        dp = new_dp
    return min(dp.values())

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, touchbar_typing()))
