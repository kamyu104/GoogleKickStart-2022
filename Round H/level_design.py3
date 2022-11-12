# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round H - Problem D. Level Design
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb1b6/0000000000c47792
#
# Time:  O(N * sqrt(N))
# Space: O(N)
#

from collections import deque

def count_of_cycle_length(P):
    lookup = [False]*len(P)
    cnt = [0]*(len(P)+1)
    for i in range(len(P)):
        l = 0
        while not lookup[i]:
            lookup[i] = True
            i = P[i]
            l += 1
        if l:
            cnt[l] += 1
    return cnt

def level_design():
    N = int(input())
    P = list(map(lambda x: int(x)-1, input().split()))
    cnt = count_of_cycle_length(P)
    dp = [INF]*(N+1)
    dp[0] = 0
    for l in range(1, N+1):
        if not cnt[l]:
            continue
        for i in range(l):
            dq = deque()
            for j in range((N-i)//l+1):
                if dq and j-dq[0][1] == cnt[l]+1:
                    dq.popleft()
                while dq and dq[-1][0] >= dp[i+j*l]-j:
                    dq.pop()
                dq.append((dp[i+j*l]-j, j))
                dp[i+j*l] = dq[0][0]+j
    mn = INF
    for l in reversed(range(1, N+1)):
        dp[l] = min(dp[l], mn+1)
        mn = min(mn, dp[l])
    return " ".join(map(str, (dp[l]-1 for l in range(1, N+1))))

INF = float("inf")
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, level_design()))
