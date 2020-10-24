class Solution:
	def addBinary(self, a: str, b: str) -> str:
		assert self.addBinary3(a,b) == self.addBinary2(a,b)

	def addBinary3(self, a: str, b: str) -> str:
		if not len(b) or not len(a):
			return a or b

		return '{0:b}'.format(int(a, base=2)+int(b, base=2))

	def addBinary2(self, a: str, b: str) -> str:
		retValBool = []
		na = [True if i == '1' else False for i in a]
		nb = [True if i == '1' else False for i in b]
		longer, shorter = (na, nb) if len(a) > len(b) else (nb, na)
		while len(longer) != len(shorter):
			shorter = [False] + shorter
		carry = False
		for i in range(len(shorter)-1, -1, -1):
			val = longer[i] ^ shorter[i] ^ carry
			carry = (longer[i] and shorter[i]) or (carry and longer[i]) or (carry and shorter[i])
			retValBool.append(val)

		if carry:
			retValBool.append(True)

		retVal = ''

		for i in reversed(list(retValBool)):
			retVal += ('1' if i else '0')

		return retVal