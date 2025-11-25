class Solution:
    def reverseQueue(self, q):
        # ToDo: Write Your Code Here. 
        stack = [None] * len(q)
        
        while q:
            stack.append(q.popleft())
        
        while stack:
            q.append(stack.pop())
            
        return q
