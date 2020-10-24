class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		facs = []
		val = 1
		for i in range(m+n):
			val *= (i+1)
			facs.append(val)

		m -= 1
		n -= 1
		npm = m+n

		return max(int(facs[npm-1]/(facs[m-1]*facs[n-1])), 1)
