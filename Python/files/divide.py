class Solution:
	def divide(self, dividend: int, divisor: int) -> int:
		if divisor == 0:
			return None

		if dividend == 0:
			return 0

		neg = (dividend >= 0) ^ (divisor >= 0)

		counter = 0

		dividend = left = abs(dividend)
		divisor = acceleratedDivisor = abs(divisor)

		acceleratedCounter = 1

		while left >= divisor:
			left -= acceleratedDivisor

			counter += acceleratedCounter

			acceleratedDivisor += acceleratedDivisor
			acceleratedCounter += acceleratedCounter

			if left < acceleratedDivisor:
				acceleratedCounter = 1
				acceleratedDivisor = divisor

		if neg:
			twiceCounter = counter + counter
			counter -= twiceCounter
			counter = max(counter, -2**31)
		else:
			counter = min(counter, 2**31-1)

		return counter 
