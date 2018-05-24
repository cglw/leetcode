# -*- coding: utf-8  -*-

# 1. Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#  You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if i != j and (nums[i] + nums[j]) == target:
                    return [i, j]
        return []


