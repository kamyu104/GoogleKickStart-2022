# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round B - Problem D. Hamiltonian Tour
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acf318
#
# Time:  O(R * C)
# Space: O(R * C)
#

def iter_dfs(R, C, B):
    result = []
    B[0//2][0//2] = '#'
    stk = [(1, ((0, 0), 0))]
    while stk:
        step, args = stk.pop()
        if step == 1:
            (r, c), i = args
            B[r//2][c//2] = '#'
            stk.append((2, ((r, c), i, 0)))
        elif step == 2:
            (r, c), i, cnt = args
            dr, dc, d = DIRECTIONS[i]
            if cnt+1 < 3:
                stk.append((2, ((r+dr, c+dc), (i+1)%4, cnt+1)))
            dr2, dc2, d2 = DIRECTIONS[(i-1)%4]
            nr, nc = r+dr2, c+dc2
            if not (0 <= nr < 2*R and 0 <= nc < 2*C and B[nr//2][nc//2] == '*'):
                result.append(d)
                continue
            result.append(d2)
            stk.append((3, (DIRECTIONS[(i+1)%4][-1],)))
            stk.append((1, ((nr, nc), (i-1)%4)))
        elif step == 3:
            last = args[0]
            result.append(last)
    return result

def hamiltonian_tour():
    R, C = map(int, input().split())
    B = [list(input()) for _ in range(R)]
    result = iter_dfs(R, C, B)
    result.append('N')
    return "".join(result) if all(x == '#' for row in B for x in row) else "IMPOSSIBLE"

DIRECTIONS = [(0, 1, 'E'), (1, 0, 'S'), (0, -1, 'W'), (-1, 0, 'N')]
for case in range(int(input())):
    print('Case #%i: %s' % (case+1, hamiltonian_tour()))
