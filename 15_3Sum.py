# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique
# triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) < 3:
            return []

        target = []

        for i in range(1, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if nums[i - 1] + nums[i] + nums[j] == 0:
                    target.append([nums[i - 1], nums[i], nums[j]])
                    break
                pass
        return target


nums = [-1, 0, 1, 2, -1, -4]
print Solution().threeSum(nums)
