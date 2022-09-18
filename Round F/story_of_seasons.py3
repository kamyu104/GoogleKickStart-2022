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
    seeds.sort(key=lambda x: D-x[1])
    result = 0
    max_heap = []
    prev = D
    for d in sorted({0}|{D-l for _, l, _ in seeds}, reverse=True):
        cnt = 0
        while cnt < (prev-d)*X and max_heap:
            v, q = heappop(max_heap)
            v = -v
            g = min((prev-d)*X-cnt, q)
            q -= g
            cnt += g
            result += g*v
            if q:
                heappush(max_heap, (-v, q))
        while seeds and D-seeds[-1][1] == d:
            q, _, v = seeds.pop()
            heappush(max_heap, (-v, q))
        prev = d
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, story_of_seasons()))
