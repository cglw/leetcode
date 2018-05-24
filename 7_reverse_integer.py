# Given a 32-bit signed integer, reverse digits of an integer.


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        res = 0
        (sign, x) = (1, x) if x > 0 else (-1, -x)
        while x != 0:
            res = res * 10 + x % 10
            if res > 2147483647:
                return 0
            x /= 10
        if (sign * res) < -2147483648:
            return 0
        return sign * res


if __name__ == '__main__':
    # a=2147483648888888888888888
    # b=2147483649999999999999999
    # print b-a
    # -2147483648
    #
    # b=3
    # print type(b)==
    #
    print   type(2147483648)
    print   type(214748364702000)
    # print Solution().reverse(190)
    # print -(1 * 10 / 10)
    print Solution().reverse(-190)
    print Solution().reverse(-2319)
    print Solution().reverse(1534236469)
    print Solution().reverse(2147483647)
    print Solution().reverse(2147483648)
    print Solution().reverse(2147483649999999999999999)
    import math
    print 0.01-0.01==0
