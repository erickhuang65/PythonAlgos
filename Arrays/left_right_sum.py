class Solution:
    def findDifferenceArray(self, nums):
        n = len(nums)
        differenceArray = [0] * n
        # TODO: Write your code here
        left_sum = 0
        right_sum = sum(nums)

        for i in range(n):
            right_sum -= nums[i] # this is to update the rightsum before by subtracting the current value
            differenceArray[i] = abs(left_sum - right_sum)
            left_sum += nums[i] # this is to update the leftsum so that leftsum captures all value before the next index
        return differenceArray

if __name__ == '__main__':
    sol = Solution()