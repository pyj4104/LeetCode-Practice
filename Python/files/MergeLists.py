# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		newHead = index = ListNode(0)

		while l1 and l2:
			if l1.val < l2.val:
				index.next = l1
				l1 = l1.next
			else:
				index.next = l2
				l2 = l2.next
			index = index.next
		
		index.next = l1 or l2

		return newHead.next
	
	def buildLL(self, nums: [int]):
		if len(nums) < 1:
			return None
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
tcs = [
[[1, 2, 4], [1, 3, 4]],
[[1, 2, 4], []],
[[], []],
[[1, 2, 4], [5]]
]
for tc in tcs:
	ll1 = s.buildLL(tc[0])
	ll2 = s.buildLL(tc[1])
	s.printLL(s.mergeTwoLists(ll1, ll2))