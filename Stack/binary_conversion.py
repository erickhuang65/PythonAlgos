class Solution: 
    def decimalToBinary(self, num):
        # ToDo: Write Your Code Here.
        # need a temp to store the divisible remainder
        # returns string of binary numbers
        if num == 0:
            return "0"
        stack = []
        while num:
            if num % 2 != 0:
                num = num // 2
                stack.append("1")
            else:
                num = num // 2
                stack.append("0")
        binary = ""
        while stack:
            binary += stack.pop()
        return binary
