class Solution:
	def combinationSum(self, candidates: [int], target: int) -> [[int]]:
		retVals = []
		self.combinationSumRec(candidates, target, [], retVals)
		return retVals

	def combinationSumRec(self, candidates: [int], target: int, retVal: [int], retVals: [[int]]):
		if target == 0:
			retVals.append(retVal)
		elif target < 0:
			pass
		else:
			retValOri = retVal.copy()
			for i, num in enumerate(candidates):
				self.combinationSumRec(candidates[i:], target-num, retValOri + [num], retVals)