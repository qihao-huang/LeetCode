# https://leetcode-cn.com/problems/rotate-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # step 1: corner cases:
        # 1. 如果 head 为空
        # 2. 如果 k == 0
        # 3. 如果 链表仅有一个元素
        # 都返回 head
    
        if (not head) or (k==0) or (not head.next):
            return head

        # step 2: 遍历得到链表元素总个数
        # 1 > 2 > 3 > 4 > 5 
        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1

        # 如果 k 是 n 的倍数，那么其实就是原状
        if k % n == 0:
            return head

        # n = 5
        # k = 2
        # step 3:
        # 此时 cur = node(5)，
        # 再将链表闭拢成环  5 > 1
        cur.next = head

        # 并从 clip_n 处切断
        clip_n = n - k % n
        # clip_n = 3

        # step 4: 
        # 遍历个数至 clip_n 个元素

        while clip_n:
            cur = cur.next
            clip_n -= 1
        
        # 返回 node(4), 4 > 5 > 1 > 2 > 3
        clip_head = cur.next

        # 3 > None
        clip_tail = cur
        clip_tail.next = None

        return clip_head

