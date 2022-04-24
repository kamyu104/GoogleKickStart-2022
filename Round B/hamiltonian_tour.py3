# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round B - Problem D. Hamiltonian Tour
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acf318
#
# Time:  O(R * C), pass in PyPy3 but Python3
# Space: O(R * C)
#

def direction(a, b, n):
    r, c = divmod(a, n)
    nr, nc = divmod(b, n)
    if nr-r == 1: return 'S'
    if nc-c == 1: return 'E'
    if nr-r == -1: return 'N'
    if nc-c == -1: return 'W'

def create_node(n, curr, nxts):
    r, c = curr
    r, c = 2*r, 2*c
    if nxts[r*n+c] != -1:
        return False
    for dr, dc in DIRECTIONS:
        nr, nc = r+dr, c+dc
        nxts[r*n+c] = nr*n+nc
        r, c = nr, nc
    return True

def merge_node(n, curr, parent, nxts):
    if curr < parent:
        curr, parent = parent, curr
    r, c = curr
    pr, pc = parent
    if r-pr:
        nxts[(2*r)*n+(2*c)] = (2*pr+1)*n+(2*c)
        nxts[(2*pr+1)*n+(2*pc+1)] = (2*r)*n+(2*c+1)
    else:
        nxts[(2*r+1)*n+(2*c)] = (2*pr+1)*n+(2*pc+1)
        nxts[(2*pr)*n+(2*pc+1)] = (2*r)*n+(2*c)

def iter_dfs(B):
    nxts = [-1]*((2*len(B))*(2*len(B[0])))
    stk = [(1, ((0, 0), None))]
    while stk:
        step, args = stk.pop()
        if step == 1:
            curr, parent = args
            if not create_node(2*len(B[0]), curr, nxts):
                continue
            if parent:
                merge_node(2*len(B[0]), curr, parent, nxts)
            stk.append((2, (curr, len(DIRECTIONS)-1)))
        elif step == 2:
            curr, i = args
            if i < 0:
                continue
            nr, nc = curr[0]+DIRECTIONS[i][0], curr[1]+DIRECTIONS[i][1]
            stk.append((2, (curr, i-1)))
            if not (0 <= nr < len(B) and 0 <= nc < len(B[0]) and B[nr][nc] == '*'):
                continue
            stk.append((1, ((nr, nc), curr)))
    return nxts

def hamiltonian_tour():
    R, C = map(int, input().split())
    B = [input() for _ in range(R)]
    nxts = iter_dfs(B)
    if sum(x != -1 for x in nxts) != 4*(R*C-sum(B[i][j] == '#' for i in range(R) for j in range(C))):
        return "IMPOSSIBLE"
    result = []
    curr, prev = 0, -1
    while prev == -1 or curr:
        prev = curr
        curr = nxts[curr]
        result.append(direction(prev, curr, 2*C))
    return "".join(result)

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, hamiltonian_tour()))
