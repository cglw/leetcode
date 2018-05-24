#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        target = []
        j = 0
        k = 0
        while True:
            if j == len(nums1) and k == len(nums2):
                break
            elif j < len(nums1) and k < len(nums2):
                if nums1[j] < nums2[k]:
                    target.append(nums1[j])
                    j += 1
                else:
                    target.append(nums2[k])
                    k += 1
            else:
                for i in range(j, len(nums1)):
                    target.append(nums1[i])
                for i in range(k, len(nums2)):
                    target.append(nums2[i])
                break
        print target
        tmid = len(target) / 2
        if len(target) % 2 == 0:
            mid = float(target[tmid - 1] + target[tmid]) / 2
        else:
            mid = target[tmid]
        return mid


if __name__ == '__main__':
    pass
    print Solution().findMedianSortedArrays([1, 2], [])
