# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round B - Problem D. Hamiltonian Tour
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caa74/0000000000acf318
#
# Time:  O(R * C), pass in PyPy3 but Python3
# Space: O(R * C)
#

class UnionFind(object):  # Time: O(n * alpha(n)), Space: O(n)
    def __init__(self, n):
        self.set = list(range(n))
        self.rank = [0]*n
        self.cnt = n

    def find_set(self, x):
        stk = []
        while self.set[x] != x:  # path compression
            stk.append(x)
            x = self.set[x]
        while stk:
            self.set[stk.pop()] = x
        return x

    def union_set(self, x, y):
        x, y = self.find_set(x), self.find_set(y)
        if x == y:
            return False
        if self.rank[x] > self.rank[y]:  # union by rank
            x, y = y, x
        self.set[x] = self.set[y]
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        self.cnt -= 1
        return True

def valid(prev, curr, edges):
    if (prev[0]//2, prev[1]//2) != (curr[0]//2, curr[1]//2):
        return True
    if prev > curr:
        prev, curr = curr, prev
    r, c = prev[0]//2, prev[1]//2
    if prev[0]%2 == curr[0]%2 == 0: return ((r-1, c), (r, c)) not in edges
    if prev[0]%2 == curr[0]%2 == 1: return ((r, c), (r+1, c)) not in edges
    if prev[1]%2 == curr[1]%2 == 0: return ((r, c-1), (r, c)) not in edges
    if prev[1]%2 == curr[1]%2 == 1: return ((r, c), (r, c+1)) not in edges

def wall_follower(B, edges):
    result = []
    lookup = [[False]*(2*len(B[0])) for _ in range(2*len(B))]
    r, c = (0, 0)
    i = 3
    while not (result and (r, c) == (0, 0)):
        for j in reversed(range(i-1, i+2)):  # right-hand rule
            j %= 4
            dr, dc, _ = DIRECTIONS[j]
            nr, nc = r+dr, c+dc
            if 0 <= nr < 2*len(B) and 0 <= nc < 2*len(B[0]) and \
               B[nr//2][nc//2] == '*' and not lookup[nr][nc] and \
               valid((r, c), (nr, nc), edges):
                break
        i = j
        r, c = r+dr, c+dc
        lookup[r][c] = True
        result.append(DIRECTIONS[i][-1])
    return result
    
def hamiltonian_tour():
    R, C = map(int, input().split())
    B = [input() for _ in range(R)]
    uf = UnionFind(R*C)
    edges = set()
    cnt = 0
    for i in range(R):
        for j in range(C):
            if B[i][j] != '*':
                cnt += 1
                continue
            if i and B[i-1][j] == '*' and uf.union_set((i-1)*C+j, i*C+j):
                edges.add(((i-1, j), (i, j)))
            if j and B[i][j-1] == '*' and uf.union_set(i*C+(j-1), i*C+j):
                edges.add(((i, j-1), (i, j)))
    return "".join(wall_follower(B, edges)) if uf.cnt-cnt == 1 else "IMPOSSIBLE"

DIRECTIONS = [(0, 1, 'E'), (1, 0, 'S'), (0, -1, 'W'), (-1, 0, 'N')]
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, hamiltonian_tour()))
