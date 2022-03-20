# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round A - Problem D. Interesting Integers
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e73ea
#
# Time:  O(M * (9M)^3), M is max(len(digits))
# Space: O(M * (9M)^3)
#

def g(l, product, total, target):  # Total Time: O(M * (9M)^3)
    if l == 0:
        return int(total == target and product == 0)
    if (l, product, total, target) not in lookup:
        lookup[(l, product, total, target)] = sum(g(l-1, (product*x)%target, total+x, target) for x in range(0, 9+1))
    return lookup[(l, product, total, target)]

def count_interesting_integers_with_number_of_digits(target, l):  # Time: O(1)
    return sum(g(l-1, x%target, x, target) for x in range(1, 9+1))

def count_interesting_integers_with_prefix_of_digits(target, digits):  # Time: O(len(digits))
    result = 0
    product, total = 1, 0
    for i in range(len(digits)+1):
        if i == len(digits):
            result += int(product%total == 0 and total == target)
            continue
        result += sum(g((len(digits)-1)-i, (product*x)%target, total+x, target) for x in range(int(i == 0), digits[i]))
        product, total = (product*digits[i])%target, total+digits[i]
    return result

def f(x):  # Time: O(len(digits)^2)
    if x == 0:
        return 0
    digits = list(map(int, str(x)))
    count = 0
    for target in range(1, 9*len(digits)+1):
        for l in range(1, len(digits)):
            count += count_interesting_integers_with_number_of_digits(target, l)
        count += count_interesting_integers_with_prefix_of_digits(target, digits)
    return count

def interesting_integers():
    A, B = list(map(int, input().strip().split()))
    return f(B)-f(A-1)

lookup = {}
for case in range(eval(input())):
    print('Case #%d: %s' % (case+1, interesting_integers()))