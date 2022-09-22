# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round F - Problem C. Story of Seasons
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb409/0000000000bef319
#
# Time:  O(NlogN)
# Space: O(N)
#

from heapq import heappush, heappop

def story_of_seasons():
    D, N, X = map(int, input().split())
    seeds = [list(map(int, input().split())) for _ in range(N)]
    seeds.sort(key=lambda x:x[1])
    if seeds[-1][1] < D:
        seeds.append((0, D, 0))
    result = prev = 0
    max_heap = []
    for Q, L, V in seeds:
        cnt, total = 0, (L-prev)*X
        while cnt < total and max_heap:
            v, q = heappop(max_heap)
            v, q = -v, -q
            c = min(total-cnt, q)
            q -= c
            cnt += c
            result += c*v
            if q:
                heappush(max_heap, (-v, -q))
        heappush(max_heap, (-V, -Q))
        prev = L
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, story_of_seasons()))
