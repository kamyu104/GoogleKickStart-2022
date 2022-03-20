# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round A - Problem B. Challenge Nine
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7997
#
# Time:  O(logN)
# Space: O(logN)
#

def challenge_nine():
    N = int(input().strip())
    s = list(map(int, str(N)))
    x = -sum(s)%9
    s.insert(next((i for i in range(int(x == 0), len(s)) if s[i] > x), len(s)), x)
    return "".join(map(str, s))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, challenge_nine()))
