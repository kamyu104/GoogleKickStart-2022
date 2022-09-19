# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round F - Problem C. Story of Seasons
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb409/0000000000bef319
#
# Time:  O(NlogN)
# Space: O(N)
#

from collections import defaultdict
from heapq import heappush, heappop

def story_of_seasons():
    D, N, X = map(int, input().split())
    seeds = [list(map(int, input().split())) for _ in range(N)]
    deadlines = defaultdict(list)
    deadlines[0] = []
    for q, l, v in seeds:
        deadlines[D-l].append((q, v))
    result = 0
    max_heap = []
    prev = D
    for d in sorted(deadlines.keys(), reverse=True):
        cnt = 0
        while cnt < (prev-d)*X and max_heap:
            v, q = heappop(max_heap)
            v, q = -v, -q
            c = min((prev-d)*X-cnt, q)
            q -= c
            cnt += c
            result += c*v
            if q:
                heappush(max_heap, (-v, -q))
        for q, v in deadlines[d]:
            heappush(max_heap, (-v, -q))
        prev = d
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, story_of_seasons()))
