# https://leetcode-cn.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 以相同形式返回一个表示和的链表。

        # n1 + n2 + carry 
        # cur_node = (n1 + n2 + carry) % 10
        # next_node_carry = floor(n1 + n2 + carry)

        # corner cases: l1 和 l2 不等长时
        # 例如 
        # l1 2 > 4 > 3 > (0)  补充 0 
        # l2 5 > 6 > 4 > 5
        
        # corner cases: 
        # l1 和 l2 末尾进位

        cur_l1 = l1
        cur_l2 = l2
        carry = 0

        import math

        head = ListNode(-1)
        prev = head

        while cur_l1 or cur_l2:
            n1 = cur_l1.val if cur_l1 else 0
            n2 = cur_l2.val if cur_l2 else 0
            
            prev.next = ListNode(-1)
            prev.next.val = (n1 + n2 + carry) % 10
            carry = math.floor((n1 + n2 + carry) / 10)

            prev = prev.next
            if cur_l1:
                cur_l1 = cur_l1.next
            if cur_l2:
                cur_l2 = cur_l2.next

        if carry > 0:
            prev.next = ListNode(carry)

        return head.next