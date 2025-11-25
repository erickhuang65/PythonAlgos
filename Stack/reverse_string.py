class Solution:
    def reverseString(self, s):
        # ToDo: Write Your Code Here.
        stack = []
        for c in s:
            stack.append(c)

        s = ""
        for val in range(len(stack)):
            s += stack.pop()
        return s

s = Solution()
print(s.reverseString("Erick"))