# coding=utf-8
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# class Solution(object):
#     def isMatch(self, text, pattern):
#         if not pattern:
#             return not text
#         first_match = bool(text) and pattern[0] in [text[0], '.']
#         if len(pattern) >= 2 and pattern[1] == '*':
#             return (self.isMatch(text, pattern[2:]) or
#                     first_match and self.isMatch(text[1:], pattern))
#         else:
#             return first_match and self.isMatch(text[1:], pattern[1:])
#




class MySolution(object):
    def test(self,text,p):
        if not p:
            return not text
        return result1



# class Solution2(object):
#     def isMatch(self, text, pattern):
#
#         for i in range(0, len(text)):
#             for j in range(0, len(pattern)):
#                 if pattern[j] in [text[i], '.']:
#                     continue
#
#
# class Solution3(object):
#     def isMatch(self, text, pattern):
#         index_t, index_p = 0, 0
#         while 1:
#             if pattern[index_p] in [text[index_t,'.']:
#                 continue
#             el
print MySolution().test('www',"w*")