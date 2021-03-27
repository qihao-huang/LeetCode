# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 遍历一遍数组
        # 如果当前元素值与下一个元素值相等，
        # 则删除下一个元素
        if not head:
            return head

        cur = head
        
        # 避免最后为空
        while cur.next:
            ## A > A > B > C 
            if cur.val == cur.next.val:
                # A > B > C
                cur.next = cur.next.next
            else:
                cur = cur.next 
        
        return head
