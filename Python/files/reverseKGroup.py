# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from basicClasses.Helper import LinkedList, ListNode, TestSuites

class Solution:
	def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
		if head is None:
			return None

		# Basic vars
		index = head
		numNodes = 0
		dummy = ListNode()

		# Count how many nodes are there
		while index:
			numNodes += 1
			index = index.next

		numGroup = int(numNodes/k)

		# Reset the index
		index = head

		dummy.next = index

		index = head

		endOfLastGroup = dummy

		groupIndex = 0
		while index:
			if groupIndex >= numGroup:
				break

			# Get the last item
			for i in range(k-1):
				index = index.next

			curEnd = index

			# Get the beginning of the next segment
			index = index.next

			# Cut the current segment
			curEnd.next = None

			# Reverse
			newSegmentHead, newSegmentTail = self.reverseLL(endOfLastGroup.next)
			
			# Connect
			endOfLastGroup.next = newSegmentHead
			newSegmentTail.next = index

			# Set Previous
			endOfLastGroup = newSegmentTail

			# Increase counter
			groupIndex += 1

		return dummy.next

	def reverseLL(self, head: ListNode) -> ListNode:
		if not head:
			return None

		prev = None
		index = next = head

		while index:
			next = next.next
			index.next = prev
			prev = index
			index = next

		index = prev

		while index.next:
			index = index.next

		return prev, index


s = Solution()
testCases = [[[1, 2, 3, 4, 5], 2], [[1, 2, 3, 4, 5], 3], [[1, 2, 3], 3]]
t = TestSuites(s, testCases, isLL = 0, numArg = 2)
t.runTests('reverseKGroup')
'''testCases = [[1, 2, 3, 4, 5], [1]]
t = TestSuites(s, testCases, isLL = True)
t.runTests('reverseLL')'''

