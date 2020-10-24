# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        i = head
        counter = 0
        heads = []
        while i:
            if counter%2==0:
                heads.append(i)
            i = i.next
            counter += 1

        dummy = index = ListNode()

        for item in heads:
            if item.next:
                index.next = item.next
                index.next.next = item
            else:
                index.next = item
            index = index.next.next

        if index:
            index.next = None

        return dummy.next

    def printLL(self, head: ListNode, counter = 0):
        nextSign = ' -> '
        retVal = 'Start'
        index = head

        while index and counter < 21:
            retVal = retVal + nextSign + str(index.val)
            index = index.next
            counter += 1

        print(retVal)

    def buildLL(self, vals: [int]) -> ListNode:
        index = dummy = ListNode()
        for val in vals:
            index.next = ListNode(val = val)
            index = index.next

        return dummy.next

s = Solution()
tcs = [[1, 2, 3, 4], [], [1, 2, 3]]
for tc in tcs:
    head = s.buildLL(tc)
    s.printLL(head)
    head = s.swapPairs(head)
    s.printLL(head)