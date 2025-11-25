class Solution:
    def findMaxOnesRow(self, mat):
        maxOnesIdx, maxOnesCount = 0, 0  # Initialize tracking variables
        # ToDo: Write Your Code Here.
        for i, row in enumerate(mat):
            current_count = sum(row)
            if maxOnesCount < current_count:
                maxOnesIdx, maxOnesCount = i, current_count
        return [maxOnesIdx, maxOnesCount]  

