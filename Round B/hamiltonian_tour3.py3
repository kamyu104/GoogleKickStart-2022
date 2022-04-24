# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round B - Problem D. Hamiltonian Tour
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acf318
#
# Time:  O(R * C)
# Space: O(R * C)
#

def direction(r, c):
    return NEXT.index((r%2, c%2))

def iter_dfs(R, C, B):
    result = []
    B[0//2][0//2] = '#'
    stk = [(1, ((0, 0),))]
    while stk:
        step, args = stk.pop()
        if step == 1:
            r, c = args[0]
            B[r//2][c//2] = '#'
            stk.append((2, ((r, c), 0)))
        elif step == 2:
            (r, c), i = args
            d = direction(r, c)
            if i == 4:
                result.pop()
                continue
            dr, dc = DIRECTIONS[d]
            stk.append((2, ((r+dr, c+dc), i+1)))
            dr, dc = DIRECTIONS[(d-1)%4]
            nr, nc = r+dr, c+dc
            if not (0 <= nr < 2*R and 0 <= nc < 2*C and B[nr//2][nc//2] == '*'):
                result.append(DIRS[d])
                continue
            result.append(DIRS[(d-1)%4])
            stk.append((3, (DIRS[((d-1)%4+2)%4],)))
            stk.append((1, ((nr, nc),)))
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

DIRS = 'ESWN'
NEXT = [(0, 0), (0, 1), (1, 1), (1, 0)]
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, hamiltonian_tour()))
