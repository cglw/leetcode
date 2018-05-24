class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        target = []
        max = pow(2, 31) - 1
        min = -pow(2, 31)
        for i in range(0, len(str)):
            index = str[i]
            if index == '-':
                if len(target) == 0:
                    target.append(index)
                else:
                    break
            elif index == '+':
                if len(target) == 0:
                    target.append(index)
                else:
                    break
            elif index == ' ':
                if len(target) > 0:
                    break
                continue
            elif 48 <= ord(index) <= 57:
                target.append(index)
                if i < len(str) - 1 and str[i + 1] == ' ':
                    continue
                elif i < len(str) - 1 and (ord(str[i + 1]) < 48 or ord(str[i + 1]) > 57):
                    break
            elif ord(index) < 48 or ord(index) > 57:
                break
        if len(target) == 0 or (len(target) == 1 and (ord(target[0]) < 48 or ord(target[0]) > 57)):
            return 0
        res = int(''.join(target))
        if res > max:
            return max
        elif res < min:
            return min
        return res


if __name__ == '__main__':
    print Solution().myAtoi('42')
    print Solution().myAtoi('-    42')
    print Solution().myAtoi('4193 with words')
    print Solution().myAtoi('words and 987')
    print Solution().myAtoi('-91283472332')
    print Solution().myAtoi('43 1231')
    print Solution().myAtoi('-')
    print Solution().myAtoi('0000000000012345678')
    print Solution().myAtoi('-+1')
    print Solution().myAtoi('   +6 123')
    # print int('--1')
