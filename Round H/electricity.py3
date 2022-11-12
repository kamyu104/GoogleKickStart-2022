# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round H - Problem C. Eelectricity
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb1b6/0000000000c47c8e
#
# Time:  O(N)
# Space: O(N)
#

def topological_sort(adj, in_degree, cb):
    q = [u for u in range(len(adj)) if not in_degree[u]]
    while q:
        new_q = []
        for u in q:
            for v in adj[u]:
                in_degree[v] -= 1
                cb(u, v)
                if in_degree[v]:
                    continue
                new_q.append(v)
        q = new_q

def electricity():
    N = int(input())
    A = list(map(int, input().split()))
    adj = [[] for _ in range(N)]
    in_degree = [0]*N
    for _ in range(N-1):
        X, Y = map(int, input().split())
        X -= 1
        Y -= 1
        if A[X] == A[Y]:
            continue
        if A[X] > A[Y]:
            X, Y = Y, X
        adj[X].append(Y)
        in_degree[Y] += 1
    dp = [1]*len(adj)
    def add_dp(u, v):
        dp[v] += dp[u]

    topological_sort(adj, in_degree, add_dp)
    return max(dp)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, electricity()))
