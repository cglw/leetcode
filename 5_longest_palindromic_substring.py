# -*- coding: utf-8  -*-

#
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example:
#
# Input: "babad"
#
# Output: "bab"
#
# Note: "aba" is also
# a
# valid
# answer.
#
# Example:
#
# Input: "cbbd"
#
# Output: "bb"

class Solution(object):
    def find_mid_longest_palindrome(self, s, mid_index=0, mid_next_index=-1):
        last_move_count = 0
        while 1:
            move_count = (last_move_count + 1)
            if mid_next_index == -1:
                if mid_index - move_count < 0 or mid_index + move_count > len(s) - 1:
                    break
                if s[mid_index - move_count] != s[mid_index + move_count]:
                    break
            else:
                if mid_next_index > mid_index:
                    if mid_index - move_count < 0 or mid_next_index + move_count > len(s) - 1:
                        break
                    if s[mid_index - move_count] != s[mid_next_index + move_count]:
                        break
                else:
                    if mid_next_index - move_count < 0 or mid_index + move_count > len(s) - 1:
                        break
                    if s[mid_next_index - move_count] != s[mid_index + move_count]:
                        break
                    pass
            last_move_count += 1
        if mid_next_index > -1:
            return s[mid_index - last_move_count:mid_next_index + last_move_count + 1]
        else:
            return s[mid_index - last_move_count:mid_index + last_move_count + 1]

    def longestPalindrome(self, s):
        if len(s) <= 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return ''
        max_length = 0
        max_length_str = ''
        same_str = []
        for i in range(0, len(s) - 1):
            if s[i] in same_str or len(same_str) <= 0:
                same_str.append(s[i])
            if s[i + 1] not in same_str or i == len(s) - 2:
                if i == len(s) - 2 and (s[i + 1] in same_str):
                    same_str.append(s[i + 1])
                    i += 1
                if len(same_str) % 2 == 0:
                    res = self.find_mid_longest_palindrome(s, i - len(same_str) / 2, i - len(same_str) / 2 + 1)
                else:
                    res = self.find_mid_longest_palindrome(s, i - len(same_str) / 2)
                same_str = []

                if len(res) > max_length:
                    max_length = len(res)
                    max_length_str = res

        return max_length_str


if __name__ == '__main__':
    # print Solution().isPalindrome("xxxbbasabbxxx")

    print Solution().longestPalindrome("xxxbbasabbxxx")
    print Solution().longestPalindrome("babad")
    print Solution().longestPalindrome("cbbd")
    print Solution().longestPalindrome("cb")
    print Solution().longestPalindrome("c")
    print Solution().longestPalindrome("cc")
    print Solution().longestPalindrome("cccc")
    print Solution().longestPalindrome("ccccc")
    # print Solution().find_mid_longest_palindrome("xxxbbasabbxxx", 2)
    # print Solution().find_mid_longest_palindrome("xxxbbasabbxxx", 1)
    # print Solution().find_mid_longest_palindrome("xxxbbasabbxxx", 4)
    # print Solution().find_mid_longest_palindrome("xxxbbasabbxxx", 5)
    # print Solution().find_mid_longest_palindrome("xxxbbasabbxxx", 6)
