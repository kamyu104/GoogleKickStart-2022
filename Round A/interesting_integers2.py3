# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round A - Problem D. Interesting Integers
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e73ea
#
# Time:  precompute: O(2835 * log(MAX_B)^2)
#        runtime:    O(9 * (logB)^2)
# Space: O(2835 * log(MAX_B)^2)
#

from functools import lru_cache

def norm(x):  # Time: O(logx)
    if x == 0:
        return 0
    for p, p_bound in FACT:
        while x%p == 0 and (x//p)%p_bound == 0:
           x //= p
    return x

@lru_cache(None)  # lazily precompute
def memoization(l, product, total):  # Total Time: O(log(MAX_B) * ((6+1)*(4+1)*(2+1)*(2+1)) * 9log(MAX_B)) = O(2835 * log(MAX_B)^2) = 56779 (by memoization.cache_info())
    if l == 0:
        return int(total and product%total == 0)
    return sum(memoization(l-1, norm(product*x), total+x) for x in range(10))

def count_with_prefix_of_digits(digits):  # Time: O(9 * len(digits)^2)
    result = 0
    product, total = 1, 0
    for i, x in enumerate(digits):
        result += sum(memoization((len(digits)-1)-i, norm(product*x), total+x) for x in range(int(i == 0), x))
        product, total = product*x, total+x
    result += memoization(0, norm(product), total)
    return result

def f(x):  # Time: O(9 * (logx)^2)
    digits = list(map(int, str(x)))
    result = 0
    for l in range(1, len(digits)):
        result += sum(memoization(l-1, norm(x), x) for x in range(1, 10))
    result += count_with_prefix_of_digits(digits)
    return result

def interesting_integers():
    A, B = list(map(int, input().strip().split()))
    return f(B)-f(A-1)

MAX_B = 10**12
MAX_TOTAL = 9*len(str(MAX_B))  # capped by 2^6 * 3^4 * 5^2 * 7^2
FACT = [[2, 1], [3, 1], [5, 1], [7, 1]]
for i in range(len(FACT)):
    while FACT[i][1]*FACT[i][0] <= MAX_TOTAL:
        FACT[i][1] *= FACT[i][0]
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, interesting_integers()))
