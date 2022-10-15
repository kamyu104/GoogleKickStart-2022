# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round G - Problem B. Curling
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb2e1/0000000000c17c82
#
# Time:  O(N + M)
# Space: O(N + M)
#

def curling():
    def scoring_stones():
        stones = []
        N = int(input())
        for _ in range(N):
            X, Y = map(int, input().split())
            if X**2+Y**2 <= R**2:
                stones.append(X**2+Y**2)
        return stones

    R = sum(map(int, input().split()))
    A, B = scoring_stones(), scoring_stones()
    min_A, min_B = min(A, default=float("inf")), min(B, default=float("inf"))
    return "%s %s" % (sum(x < min_B for x in A), sum(x < min_A for x in B))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, curling()))
