# Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        p1 = l1
        p2 = l2

        l3 = ListNode()
        p3 = l3

        over10 = False

        while p1 or p2:

            if p1 and p2:
                val = p1.val + p2.val

                if over10:
                    val += 1
                    over10 = False

                if val > 9:
                    over10 = True
                    val %= 10

                p1, p2 = p1.next, p2.next

            elif p1:
                val = p1.val
                if over10:
                    val += 1
                    over10 = False

                if val > 9:
                    val %= 10
                    over10 = True

                p1 = p1.next


            elif p2:
                val = p2.val

                if over10:
                    val += 1
                    over10 = False

                if val > 9:
                    val %= 10
                    over10 = True

                p2 = p2.next

            p3.next = ListNode(val)
            p3 = p3.next

        if over10:
            p3.next = ListNode(1)

        return l3.next