class Solution:
    def runningSum(self, nums):
        # check for edge cases
        if nums is None or len(nums) == 0:
            return []
        # define the result array that has the same length as nums to store vals
        result = [0] * len(nums)  
        # TODO: Write your code here
        # setting index 0 in result to the first value of nums
        total = nums[0]
        result[0] = nums[0]
        # set i to the second value of the array
        for i in range(1, len(nums)):
            total += nums[i]
            result[i] = total
        return result
