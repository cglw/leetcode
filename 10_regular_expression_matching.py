class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        print pattern[0],text[0],bool(text)
        first_match = bool(text) and pattern[0] in [text[0], '.']
        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


class Solution2(object):
    def isMatch(self, text, pattern):

        for i in range(0, len(text)):
            for j in range(0, len(pattern)):
                if pattern[j] in [text[i], '.']:
                    continue


# print Solution().isMatch("aa", "a*")
# print Solution().isMatch("aab", "*a*")
# print Solution().isMatch("ab", "a.*")
print Solution().isMatch("aab", "c*a*b")


# print not ''
# data = ''
# for i in range(0, 1000*1000):
#     data += 'a'
#
# print Solution().isMatch(data, "mis*is*p*.")
