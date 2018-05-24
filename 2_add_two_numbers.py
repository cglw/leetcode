# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = ListNode(0)
        curr = head
        while l1 is not None or l2 is not None:
            x = 0 if l1 is None else l1.val
            y = 0 if l2 is None else l2.val
            sum = carry + x + y
            carry = sum / 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next


if __name__ == '__main__':
    l0 = ListNode(2)
    l1 = l0
    list = [4, 3]
    for data in list:
        l = ListNode(data)
        l0.next = l
        l0 = l
    l00 = ListNode(5)
    l2 = l00
    list = [6, 4]
    for data in list:
        l = ListNode(data)
        l00.next = l
        l00 = l

    Solution().addTwoNumbers(l1, l2)
