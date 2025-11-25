class Solution:
    def simplifyPath(self, path):
        # component = path.split("/")
        # stack = []
        # for i in component:
        #     if i == "":
        #         continue
        #     elif i == ".":
        #         continue
        #     elif i == "..":
        #         stack.pop()
        #     else:
        #         stack.append(i)
        stack = []
        for i in path.split("/"):
            if i == "..":
                if stack:
                    stack.pop()
            elif i and i != ".":
                stack.append(i)
        return "/" + "/".join(stack)
    
s = Solution()
print(s.simplifyPath("/a//b////c/d//././/.."))
