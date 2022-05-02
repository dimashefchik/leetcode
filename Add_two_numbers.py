# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        solution = ListNode(0)
        head = solution
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            cur_sum = val1 + val2 + carry

            if cur_sum > 9:
                carry = 1
                cur_sum -= 10
            else:
                carry = 0

            solution.next = ListNode(cur_sum)

            solution = solution.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next
