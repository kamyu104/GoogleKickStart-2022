# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round D - Problem A. Image Labeler
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008caea6/0000000000b76e11
#
# Time:  O(N)
# Space: O(1)
#

from random import seed, randint

def nth_element(nums, left, n, right, compare=lambda a, b: a < b):
    def tri_partition(nums, left, right, target, compare):
        mid = left
        while mid <= right:
            if nums[mid] == target:
                mid += 1
            elif compare(nums[mid], target):
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
        return left, right

    while left <= right:
        pivot_idx = randint(left, right)
        pivot_left, pivot_right = tri_partition(nums, left, right, nums[pivot_idx], compare)
        if pivot_left <= n <= pivot_right:
            return
        elif pivot_left > n:
            right = pivot_left-1
        else:  # pivot_right < n.
            left = pivot_right+1

def image_labeler():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    nth_element(A, 0, (N-(M-1))-1, N-1)
    nth_element(A, 0, (0+((N-(M-1))-1))//2, (N-(M-1))-1)
    nth_element(A, (0+((N-(M-1))-1))//2+1, (0+((N-(M-1))-1))//2+1, (N-(M-1))-1)
    return (A[(0+((N-(M-1))-1))//2] if (N-(M-1))%2 else (A[(0+((N-(M-1))-1))//2]+A[(0+((N-(M-1))-1))//2+1])/2.0) + sum(A[~i] for i in range(M-1))

seed(0)
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, image_labeler()))
