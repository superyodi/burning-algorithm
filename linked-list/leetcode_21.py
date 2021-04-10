# 21. Merge Two Sorted Lists

# Definition for singly-linked list.


from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# [Try 1: Accepted]	32 ms	14.2 MB
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        nums = []

        while l1 or l2:

            if not l1:
                nums.append(l2.val)
                l2 = l2.next

            elif not l2:
                nums.append(l1.val)
                l1 = l1.next

            elif l1.val <= l2.val:
                nums.append(l1.val)

                l1 = l1.next

            else:
                nums.append(l2.val)

                l2 = l2.next

        if not nums:
            return None

        nums = deque(nums)

        merge_list = ListNode(nums.popleft())
        head = merge_list

        while nums:
            merge_list.next = ListNode(nums.popleft())
            merge_list = merge_list.next

        # print(head)

        return head

# [Try 2] 파.알.인 예시코든데 이해를 못하겠다. 획기적인건 확실

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1

