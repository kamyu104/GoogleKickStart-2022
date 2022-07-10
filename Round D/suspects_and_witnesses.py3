# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round D - Problem D. Suspects and Witnesses
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76db9
#
# Time:  O(N * K), pass in PyPy3 but Python3
# Space: O(M + K)
#

def bfs(K, adj, i):
    q = [i]
    lookup = {i}
    while q:
        new_q = []
        for u in q:
            for v in adj[u]:
                if v in lookup:
                    continue
                lookup.add(v)
                if len(lookup) > K:
                    return True
                new_q.append(v)
        q = new_q
    return False

def suspects_and_witnesses():
    N, M, K = list(map(int, input().split()))
    adj = [[] for _ in range(N)]
    for _ in range(M):
        A, B = list(map(int, input().split()))
        adj[B-1].append(A-1)
    return sum(bfs(K, adj, i) for i in range(N))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, suspects_and_witnesses()))
