class Solution:
    def isValid(self, s):
        # ToDo: Write Your Code Here.
        stack = []
        for c in s:
            # check for only open parenthesis
            # loop through s and pop only the closing parenthesis strings
            # reverse() the remaining values in s and compare it with tempStack and return True if condition met
            if c in ['(','[','{']:
                stack.append(c)
            else:
                if not stack:
                    return False
    
                top = stack.pop()
            
                if c == ')' and top != '(':
                    return False
                if c == '}' and top != '{':
                    return False
                if c == ']' and top != '[':
                    return False
                    
        return not stack
