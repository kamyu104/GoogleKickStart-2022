# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round G - Problem D. Cute Little Butterfly
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb2e1/0000000000c17b68
#
# Time:  O(NlogN), pass in PyPy3 but Python3 in test set 3
# Space: O(N)
#

from collections import defaultdict

# Template:
# https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/longest-increasing-subsequence-ii.py
class SegmentTree(object):
    def __init__(self, N,
                 build_fn=lambda _: float("-inf"),  # modified
                 query_fn=lambda x, y: y if x is None else x if y is None else max(x, y),
                 update_fn=lambda x: x):
        self.tree = [None]*(2*2**((N-1).bit_length()))
        self.base = len(self.tree)//2
        self.query_fn = query_fn
        self.update_fn = update_fn
        for i in range(self.base, self.base+N):
            self.tree[i] = build_fn(i-self.base)
        for i in reversed(range(1, self.base)):
            self.tree[i] = query_fn(self.tree[2*i], self.tree[2*i+1])

    def update(self, i, h):
        x = self.base+i
        self.tree[x] = self.update_fn(h)
        while x > 1:
            x //= 2
            self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2+1])

    def query(self, L, R):
        if L > R:
            return float("-inf")  # modified
        L += self.base
        R += self.base
        left = right = None
        while L <= R:
            if L & 1:
                left = self.query_fn(left, self.tree[L])
                L += 1
            if R & 1 == 0:
                right = self.query_fn(self.tree[R], right)
                R -= 1
            L //= 2
            R //= 2
        return self.query_fn(left, right)

def cute_little_butterfly():
    N, E = map(int, input().split())
    lookup = defaultdict(list)
    X_set = set()
    for _ in range(N):
        X, Y, C = map(int, input().split())
        lookup[Y].append((X, C))
        X_set.add(X)
    X_to_idx = {x:i for i, x in enumerate(sorted(X_set))}
    dp = [SegmentTree(len(X_to_idx)) for _ in range(2)]
    dp[0].update(0, 0)
    dp[1].update(len(X_to_idx)-1, -E)
    for Y in sorted(lookup.keys(), reverse=True):
        lookup[Y].sort()
        for X, C in lookup[Y]:
            dp[0].update(X_to_idx[X], dp[0].query(0, X_to_idx[X])+C)
        for X, C in reversed(lookup[Y]):
            dp[1].update(X_to_idx[X], dp[1].query(X_to_idx[X], len(X_to_idx)-1)+C)
        mx = [dp[0].tree[1], dp[1].tree[1]]
        dp[0].update(0, max(dp[0].query(0, 0), mx[1]-E))
        dp[1].update(len(X_to_idx)-1, max(dp[1].query(len(X_to_idx)-1, len(X_to_idx)-1), mx[0]-E))
    return max(dp[0].tree[1], dp[1].tree[1])

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, cute_little_butterfly()))
