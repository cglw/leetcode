class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        for i in range(len(x) / 2):
            if x[i] != x[len(x) - 1 - i]:
                return False
        return True


print Solution().isPalindrome(121)
print Solution().isPalindrome(-121)
print Solution().isPalindrome(10)
print Solution().isPalindrome(-0)
print Solution().isPalindrome(1001)
print Solution().isPalindrome(101)
