# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from basicClasses.Helper import ListNode, TestSuites

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        index = head
        nodeBefore = head

        for i in range(n):
            index = index.next

        if index:
            index = index.next
            while index:
                index = index.next
                nodeBefore = nodeBefore.next
            nodeToDelete = nodeBefore.next
            nodeBefore.next = nodeBefore.next.next
        else:
            nodeToDelete = head
            head = nodeBefore.next

        del(nodeToDelete)
        return head

    def buildLL(self, nums: [int]):
        head = ListNode(val = nums[0])
        index = head
        for num in nums[1:]:
            index.next = ListNode(val = num)
            index = index.next

        return head

    def printLL(self, head: ListNode):
        retVal = []
        index = head
        while index:
            retVal.append(index.val)
            index = index.next
        print(retVal)

s = Solution()
testCases = [[[1, 2, 3, 4, 5], 2], [[1, 2, 3, 4, 5], 1], [[1], 1], [[1, 2], 1], [[1, 2], 2]]

for tc in testCases:
    ll = s.buildLL(tc[0])
    ll = s.removeNthFromEnd(ll, tc[1])
    s.printLL(ll)

