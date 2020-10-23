class Solution:
	def plusOne(self, digits: [int]) -> [int]:
		if not digits:
			return [1]

		carry = 0
		digits[len(digits)-1] += 1
		for i, digit in reversed(list(enumerate(digits))):
			print(digits)
			digits[i] = (digit+carry)%10
			if (digit + carry) > 9:
				carry = 1
			else:
				carry = 0
		if carry == 1:
			digits = [1] + digits

		return digits
