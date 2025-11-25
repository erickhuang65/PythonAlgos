from queue import Queue

class Solution: 
    def generateBinaryNumbers(self, n):
        q = Queue()
        q.put("1")

        res = []
        while n > 0:
            res.append(q.get())  # Add the current binary number to the result list.
            s1 = res[-1] + "0"  # Generate the next binary number by adding "0".
            s2 = res[-1] + "1"  # Generate the next binary number by adding "1".
            q.put(s1)  # Enqueue the first generated binary number.
            q.put(s2)  # Enqueue the second generated binary number.
            n -= 1

        return res

# Testing
sol = Solution()
print(sol.generateBinaryNumbers(2))
print(sol.generateBinaryNumbers(3))
print(sol.generateBinaryNumbers(5))
