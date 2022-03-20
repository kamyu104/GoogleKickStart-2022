# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round A - Problem D. Interesting Integers
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e73ea
#
# Time:  precompute: O(log(MAX_B) * (9log(MAX_B))^3)
#        runtime:    O((9logB)^2)
# Space: O(log(MAX_B) * (9log(MAX_B))^3)
#

from functools import lru_cache

@lru_cache(None)  # lazily precompute
def memoization(target, l, product, total):  # Total Time: O(log(MAX_B) * (9log(MAX_B))^3)
    if l == 0:
        return int(total == target and product == 0)
    return sum(memoization(target, l-1, (product*x)%target, total+x) for x in range(10))

def count_with_prefix_of_digits(target, digits):  # Time: O(9 * len(digits))
    result = 0
    product, total = 1, 0
    for i, x in enumerate(digits):
        result += sum(memoization(target, (len(digits)-1)-i, (product*x)%target, total+x) for x in range(int(i == 0), x))
        product, total = (product*x)%target, total+x
    result += memoization(target, 0, product, total)
    return result

def f(x):  # Time: O((9logx))^2)
    digits = list(map(int, str(x)))
    result = 0
    for target in range(1, 9*len(digits)+1):
        for l in range(1, len(digits)):
            result += sum(memoization(target, l-1, x%target, x) for x in range(1, 10))
        result += count_with_prefix_of_digits(target, digits)
    return result

def interesting_integers():
    A, B = list(map(int, input().strip().split()))
    return f(B)-f(A-1)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, interesting_integers()))
