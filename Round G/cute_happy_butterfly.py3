# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round G - Problem D. Cute Happy Butterfly
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb2e1/0000000000c17b68
#
# Time:  O(NlogN), pass in PyPy3 but Python3 in test set 3
# Space: O(N)
#

from collections import defaultdict

class SegmentTree(object):
    def __init__(self, N,
                 build_fn=lambda _: float("-inf"),                       # modified
                 query_fn=lambda x, y: y if x is None else max(x, y),    # modified
                 update_fn=lambda x, y: y if x is None else max(x, y)):  # modified
        self.tree = [None]*(2*N)
        self.lazy = [None]*len(self.tree)
        self.base = len(self.tree)//2
        self.H = (self.base-1).bit_length()
        self.query_fn = query_fn
        self.update_fn = update_fn
        for i in range(self.base, self.base+N):
            self.tree[i] = build_fn(i-self.base)
        for i in reversed(range(1, self.base)):
            self.tree[i] = query_fn(self.tree[2*i], self.tree[2*i+1])

    def __apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.base:
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    def __push(self, x):
        n = 2**self.H
        while n != 1:
            y = x // n
            if self.lazy[y] is not None:
                self.__apply(y*2, self.lazy[y])
                self.__apply(y*2 + 1, self.lazy[y])
                self.lazy[y] = None
            n //= 2

    def update(self, L, R, h):
        def pull(x):
            while x > 1:
                x //= 2
                self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2+1])
                if self.lazy[x] is not None:
                    self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])

        if L > R:
            return
        L += self.base
        R += self.base
        L0, R0 = L, R
        while L <= R:
            if L & 1:
                self.__apply(L, h)
                L += 1
            if R & 1 == 0:
                self.__apply(R, h)
                R -= 1
            L //= 2
            R //= 2
        pull(L0)
        pull(R0)

    def query(self, L, R):
        result = float("-inf")  # modified
        if L > R:
            return result

        L += self.base
        R += self.base
        self.__push(L)
        self.__push(R)
        while L <= R:
            if L & 1:
                result = self.query_fn(result, self.tree[L])
                L += 1
            if R & 1 == 0:
                result = self.query_fn(result, self.tree[R])
                R -= 1
            L //= 2
            R //= 2
        return result

def cute_happy_butterfly():
    N, E = map(int, input().split())
    lookup = defaultdict(list)
    lookup[Y0].append((X0, C0))
    X_set = {X0}
    for _ in range(N):
        X, Y, C = map(int, input().split())
        lookup[Y].append((X, C))
        X_set.add(X)
    X_to_idx = {x:i for i, x in enumerate(sorted(X_set))}
    dp = [SegmentTree(len(X_to_idx)) for _ in range(2)]
    dp[0].update(0, 0, 0)
    for Y in sorted(lookup.keys(), reverse=True):
        lookup[Y].sort()
        for X, C in lookup[Y]:
            dp[0].update(X_to_idx[X], len(X_to_idx)-1, dp[0].query(X_to_idx[X], X_to_idx[X])+C)
        for X, C in reversed(lookup[Y]):
            dp[1].update(0, X_to_idx[X], dp[1].query(X_to_idx[X], X_to_idx[X])+C)
        mx = [dp[i].tree[1] for i in range(2)]
        for i in range(2):
            dp[i].update(0, len(X_to_idx)-1, mx[i^1]-E)
    return max(dp[i].tree[1] for i in range(2))

X0, Y0, C0 = 0, 10**18, 0
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, cute_happy_butterfly()))
