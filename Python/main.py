#from matplotlib import pyplot as plt
from files.findRepeatedDnaSequences import Solution
from files.basicClasses.Helper import List, LinkedList, ListNode, TestSuites
'''
def graphRunTime():
	s = Solution()
	testCases = []
	x = [x+1 for x in range(12)]
	for i in x:
		curVal = 1
		testCase = []
		for j in range(i):
			testCase.append(j+1)
		testCases.append(testCase)
	t = TestSuites(s, testCases, isLL = None, numArg = 1, retIndex = 0)
	y = t.compTime('permute', 10)
	plt.plot(x,y)
	plt.ylabel("in s")
	plt.show()

def compFunctions():
	s = Solution()
	testCases = [i+1 for i in range(100)]
	t = TestSuites(s, testCases, isLL = None, numArg = 1, retIndex = 1)
	t1Val = []
	t2Val = []
	for tc in testCases:
		results = t.compareFuncs(s.climbStairsF, s.dynamic, tc)
		t1Val.append(results[0])
		t2Val.append(results[1])
	plt.plot(testCases, t1Val, label='F')
	plt.plot(testCases, t2Val, label='dynamic')
	plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',ncol=2, mode="expand", borderaxespad=0.)
	plt.ylabel('in ms')
	plt.show()
'''
def test():
	s = Solution()
	testCases = ['AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT']
	t = TestSuites(s, testCases, isLL = False, numArg = 1, hasRetVal = True, retIndex = 0)
	t.runTests('findRepeatedDnaSequences')

if __name__=='__main__':
	test()
	#graphRunTime()
	#compFunctions()
	#testLL()
