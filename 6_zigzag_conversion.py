# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".



class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        index = 0
        save = []
        for i in range(0, numRows):
            save.append([])

        dir_bottom = True
        for i in range(0, len(s)):
            inner = save[index]
            inner.append(s[i])
            if dir_bottom:
                if index == numRows - 1:
                    index -= 1
                    dir_bottom = False
                else:
                    index += 1
            else:
                if index == 0:
                    index += 1
                    dir_bottom = True
                else:
                    index -= 1
        target = ''
        for data in save:
            target += ''.join(data)
        return target


# P   I   N
# A L S I G
# Y A H R
# P   I


if __name__ == '__main__':
    print Solution().convert("PAYPALISHIRING", 2)
    print Solution().convert("PAYPALISHIRING", 1)
