import sys

sys.path.append("..")

from Python.files.basicClasses.Helper import ListNode
from random import randint

class Algorithm:
	def returnRandomFromLLUisngReservoirSampling(self, head: ListNode) -> int:
		resultNode, index, indexNum = head, head.next, 1
		while index:
			if randint(0, indexNum) == 0:
				resultNode = index
			indexNum += 1
			index = index.next
		return resultNode.val
