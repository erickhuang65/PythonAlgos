class Solution:
    def diagonalSum(self, mat):
        total_sum = 0  # Initialize the total sum
        # ToDo: Write Your Code Here.
        for i in range(len(mat)):
            total_sum += mat[i][i] + mat[i][len(mat) - 1 - i]

        if len(mat) % 2 != 0:
            middle = len(mat) / 2
            total_sum -= mat[middle][middle]
        return total_sum  # Return the calculated total sum
    