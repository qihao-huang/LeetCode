# Given a linked list, determine if it has a cycle in it.
# To represent a cycle in the given linked list, 
# we use an integer pos which represents the position (0-indexed) 
# in the linked list where tail connects to. If pos is -1, 
# then there is no cycle in the linked list.

# Can you solve it using O(1) (i.e. constant) memory?

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

def stringToIntegerList(input):
    import json
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
            head = stringToListNode(line)
            line = next(lines)
            pos = int(line)
            
            ret = Solution().hasCycle(head, pos)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()

# head = [3,2,0,-4]
# pos = 1
# ret = Solution().hasCycle(head, pos)
# print(ret)