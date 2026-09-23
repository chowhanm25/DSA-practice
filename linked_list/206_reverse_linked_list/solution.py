"""
LeetCode 206: Reverse Linked List
Approach: Iterative pointer reversal
Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        current = head

        while current:
            next_node = current.next   # save where we're going
            current.next = prev        # reverse the arrow
            prev = current              # move prev forward
            current = next_node         # move current forward
        return prev