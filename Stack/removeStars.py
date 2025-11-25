class Solution:
    def removeStars(self, s):
        # ToDo: Write Your Code Here.
        # initialize stack
        stack = []
        for c in s:
            if c == "*":
                if len(stack) != 0:
                    stack.pop()
            if c != "*":
                stack.append(c)
        return "".join(stack)


if __name__ == '__main__':
    s = Solution()
    print(s.removeStars("abc*de*f"))
