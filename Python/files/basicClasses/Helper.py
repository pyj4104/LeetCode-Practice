import time
import concurrent.futures

class ListNode:
	def __init__(self, val=0, next = None):
		self.val = val
		self.next = next

	def __str__(self):
		nextVal = str(self.next) if self.next else "End"
		retVal = str(self.val) + " -> " + str(nextVal)
		return retVal

class LinkedList:
	def __init__(self, vals: []):
		index = dummy = ListNode()
		for val in vals:
			index.next = ListNode(val = val)
			index = index.next
		self.head = dummy.next

	def __str__() -> None:
		retVal = "Start -> "
		retVal += str(self.head)
		print(retVal)

class TestSuites:
	def __init__(self, s, tcs, isLL = False, numArg = 1, retIndex = 0):
		self.solution = s
		self.tcs = tcs
		self.isLL = isLL
		self.numArg = numArg
		self.retIndex = retIndex

	def runTests(self, solName: str):
		funcToTest = getattr(self.solution, solName)
		for tc in self.tcs:
			tc = self.__preprocessing__(tc)
			if self.numArg > 1:
				val = funcToTest(*tc)
				if val is None:
					val = tc[self.retIndex]
			else:
				val = funcToTest(*[tc])
				if val is None:
					val = tc
			print(val)

	def getTime(self, func, tc):
		tc = self.__preprocessing__(tc)
		startT = time.time()
		if self.numArg > 1:
			func(*tc)
			position = len(tc[0])
		else:
			func(*[tc])
			position = len(tc)
		return (time.time()-startT), position

	def compareFuncs(self, func1, func2, tc):
		tc = self.__preprocessing__(tc)
		startT1 = time.time()
		r1 = func1(tc)
		endT1 = time.time()
		startT2 = time.time()
		r2 = func2(tc)
		endT2 = time.time()
		assert r1 == r2
		return endT1-startT1, endT2-startT2

	def compTime(self, solName: str, threadNumber=2):
		funcToTest = getattr(self.solution, solName)
		runTimes = [0]*len(self.tcs)
		print(runTimes)
		with concurrent.futures.ThreadPoolExecutor(max_workers=threadNumber) as executor:
			jobs = {executor.submit(self.runTime, funcToTest, tc): tc for tc in self.tcs}
			for completedJob in concurrent.futures.as_completed(jobs):
				data = completedJob.result()
				runTimes[data[1]-1] = data[0]
				print(data)
		return runTimes

	def __preprocessing__(self, tc):
		if self.isLL is not None:
			if self.numArg > 1:
				tc[0] = LinkedList(tc[0]).head
			else:
				tc = LinkedList(tc).head
		return tc

class List(type([])):
	pass

class Helper:
	def PrintMatrix(matrix: [[]]) -> None:
		print('---')
		for row in matrix:
			print(row)
		print('---')