class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumtotal = 0

        for i in range(len(nums)):
            sumtotal = nums[i] + sumtotal
            nums[i] = sumtotal
        return nums