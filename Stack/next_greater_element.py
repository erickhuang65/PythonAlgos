class Solution:
    def nextLargerElement(self, arr):
        res = [-1]*len(arr)
        # ToDo: Write Your Code Here.
        s = []
        # loop from the end of the array
        for i in range(len(arr) -1, -1, -1):
            # checks if current val in arr is smaller than top val in s
            while s and s[-1] <= arr[i]:
                s.pop()
            # if stack is not empty; update res to the current val in s
            if s:
                res[i] = s[-1]
            # checks the current val in the arr
            s.append(arr[i])
        return res