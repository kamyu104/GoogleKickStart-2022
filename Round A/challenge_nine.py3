# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round A - Problem B. Challenge Nine
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7997
#
# Time:  O(N)
# Space: O(1)
#

def challenge_nine():
    n = int(input().strip())
    s = list(map(int, str(n)))
    x = (9-sum(s))%9
    for i in range(int(x == 0), len(s)):
        if x < s[i]:
            s.insert(i, x)
            break
    else:
        s.insert(len(s), x)
    return "".join(map(str, s))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, challenge_nine()))
