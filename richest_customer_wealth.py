class Solution:
	def maximumWealth(self, accounts: List[List[int]]) -> int:
		maxWealth = 0

		for i in accounts:
			maxWealth = max(sum(i), maxWealth)
		return maxWealth
			