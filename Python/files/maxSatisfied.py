class Solution:
	def maxSatisfied(self, customers: [int], grumpy: [int], X: int) -> int:
		if not customers:
			return 0

		numSatisfiedCustomer = 0
		for i, val in enumerate(customers):
			numSatisfiedCustomer += val if not grumpy[i] else 0

		for i in range(X):
			numSatisfiedCustomer += customers[i] if grumpy[i] else 0

		maxNumSatisfiedCustomer = numSatisfiedCustomer

		for i in range(X, len(customers)):
			numSatisfiedCustomer -= customers[i-X] if grumpy[i-X] else 0
			numSatisfiedCustomer += customers[i] if grumpy[i] else 0
			maxNumSatisfiedCustomer = max(numSatisfiedCustomer, maxNumSatisfiedCustomer)

		return maxNumSatisfiedCustomer
'''
 0 1 2 3 4 5 6 7
[1,0,1,2,1,1,7,5]
[0,1,0,1,0,1,0,1]

0, 10
1, 10
2, 10
3, 12
4, 14
5, 16
6, 16
7, 18
'''


