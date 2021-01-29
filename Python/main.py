#from matplotlib import pyplot as plt
from files.eatenApples import Solution
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
	testCases = [[[9,10,1,7,0,2,1,4,1,7,0,11,0,11,0,0,9,11,11,2,0,5,5], [3,19,1,14,0,4,1,8,2,7,0,13,0,13,0,0,2,2,13,1,0,3,7]]]
	t = TestSuites(s, testCases, isLL = False, numArg = 2, hasRetVal = True, retIndex = 0)
	t.runTests('eatenApples')

if __name__=='__main__':
	test()
	#graphRunTime()
	#compFunctions()
	#testLL()


