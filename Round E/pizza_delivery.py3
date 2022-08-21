# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round E - Problem B. Students and Mentors
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb0f5/0000000000ba84ae
#
# Time:  O(M * N^2 * 2^P)
# Space: O(N^2 * 2^P)
#

from operator import add, sub, mul, floordiv
from collections import defaultdict

def pizza_delivery():
    N, P, M, Ar, Ac = list(map(int, input().split()))
    Ar -= 1
    Ac -= 1
    OP = ['']*4
    K = [0]*4
    for i in range(4):
        OP[i], K[i] = input().split()
        K[i] = int(K[i])
    COINS = {}
    for i in range(P):
        X, Y, C = list(map(int, input().split()))
        X -= 1
        Y -= 1
        COINS[X, Y] = (C, i)
    result = -INF
    q = {(Ar, Ac, 0):0}
    while M >= 0:
        new_q = defaultdict(lambda:-INF)
        for (r, c, mask), coin in q.items():
            if mask == (1<<P)-1:
                result = max(result, coin)
            if M == 0:
                continue
            for i, (dr, dc) in enumerate(DIRECTIONS):
                nr, nc = r+dr, c+dc
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                new_mask = mask
                new_coin = OPS[OP[i]](coin, K[i])
                new_q[nr, nc, new_mask] = max(new_q[nr, nc, new_mask], new_coin)
                if not ((nr, nc) in COINS and (mask&(1<<COINS[nr, nc][1])) == 0):
                    continue
                new_mask |= 1<<COINS[nr, nc][1]
                new_coin += COINS[nr, nc][0]
                new_q[nr, nc, new_mask] = max(new_q[nr, nc, new_mask], new_coin)
        q = new_q
        M -= 1
    return result if result != -INF else "IMPOSSIBLE"

INF = float("inf")
OPS = {'+':add, '-':sub, '*':mul, '/':floordiv}
DIRECTIONS = ((-1, 0), (0, 1), (0, -1), (1, 0))
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, pizza_delivery()))
