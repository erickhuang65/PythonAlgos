class Solution:
    def makeGood(self, s):
        # ToDo: Write Your Code Here.
        # initialize an empty stack
        stack = []
        for c in s:
            if stack and stack[-1].swapcase() == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


if __name__ == '__main__':
    s = Solution()
    print(s.makeGood("AaBCcdEeff"))
    print(s.makeGood("AaBCcdEeff"))