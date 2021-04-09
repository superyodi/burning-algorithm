from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# [Try 1: Accepted] 768 ms	47.4 MB
class Solution1:
    def isPalindrome(self, head: ListNode) -> bool:
        val_list = deque()

        while head:
            val_list.append(head.val)
            head = head.next

        while len(val_list) > 1:
            if val_list.pop() != val_list.popleft():
                return False

        return True


# [Try 2: Accepted]	652 ms	31.5 MB
class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:

        fast = head;
        slow = head
        reverse = None

        while fast and fast.next:
            fast = fast.next.next
            reverse, reverse.next, slow = slow, reverse, slow.next

        if fast:
            slow = slow.next

        while slow:
            if slow.val != reverse.val:
                return False
            slow, reverse = slow.next, reverse.next

        return True