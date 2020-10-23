# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        vals = []
        for ll in lists:
            index = ll
            while index:
                vals.append(index.val)
                index = index.next
        vals.sort()
        dummy = ListNode()
        for val in vals:
            dummy.next = ListNode(val=val)
        return dummy.next