# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.

# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Runtime: 44 ms, faster than 8.21% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mergeRoot = ListNode(0)
        ptr = mergeRoot
        cur_l1 = l1
        cur_l2 = l2

        while True:
            if (not cur_l1) and (not cur_l2):
                break
            elif not cur_l1:
                while cur_l2:
                    ptr.next = ListNode(cur_l2.val)
                    ptr = ptr.next
                    cur_l2 = cur_l2.next
                break
            elif not cur_l2:
                while cur_l1:
                    ptr.next = ListNode(cur_l1.val)
                    ptr = ptr.next
                    cur_l1 = cur_l1.next
                break

            if cur_l1.val <= cur_l2.val:
                ptr.next = ListNode(cur_l1.val)
                ptr = ptr.next
                cur_l1 = cur_l1.next
            else:
                ptr.next = ListNode(cur_l2.val)
                ptr = ptr.next
                cur_l2 = cur_l2.next

        ptr = mergeRoot.next
        return ptr

def stringToListNode(numbers):
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

s1 = [1,2,4]
s2 = [1,3,4]
l1 = stringToListNode(s1)
l2 = stringToListNode(s2)

ret = Solution().mergeTwoLists(l1, l2)
out = listNodeToString(ret)
print(out)