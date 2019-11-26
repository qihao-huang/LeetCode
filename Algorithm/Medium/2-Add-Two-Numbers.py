# Runtime: 68 ms, faster than 90.96% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Add Two Numbers.

import json

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        headNode = ListNode(0)
        curr = headNode
        carry = 0

        # it should be OR not AND as a condition
        while l1!=None or l2!=None:
            if l1!=None:
                x = l1.val
            else:
                x = 0

            if l2!=None:
                y = l2.val
            else:
                y = 0
            
            sumVal = x + y + carry
            carry = sumVal // 10
            curr.next = ListNode(sumVal%10)
            curr = curr.next
            if l1!=None:
                l1 = l1.next
            if l2!=None:
                l2 = l2.next

        # be careful about this final carry as an edge case
        if carry > 0:
            curr.next = ListNode(carry)

        return headNode.next

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            l1 = stringToListNode(line)
            line = next(lines)
            l2 = stringToListNode(line)
            
            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()