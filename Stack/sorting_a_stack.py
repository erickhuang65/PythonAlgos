class Solution:
    def sortStack(self, stack):
        # use only append() and pop()
        tmpStack = []
        # if the top element of tmpStack is larger than current element in stack,
        # move the current element to the back of stack with append()
        while stack:
            temp = stack.pop()

            while tmpStack and tmpStack[-1] > temp:
                stack.append(tmpStack.pop())

            tmpStack.append(temp)
        return tmpStack