from .basicClasses.Helper import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def rotateRight(self, head: ListNode, k: int) -> ListNode:
		if not head:
			return head
		i = head
		n = 0
		while i != None:
			n += 1
			i = i.next
		if k%n == 0 or n == 1:
			return head

		numShifts = k%n

		dummy = ListNode()
		newTail = head
		index = head

		for i in range(numShifts):
			index = index.next

		while index.next:
			index = index.next
			newTail = newTail.next

		dummy.next = newTail.next
		index.next = head
		newTail.next = None

		return dummy.next
