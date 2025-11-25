from collections import deque

class Solution:
    # Constructor to initialize the queues
    def __init__(self):
        # ToDo: Write Your Code Here.
        # queues will behave like a stack
        # queue 1 will hold elemnts in stack order
        # queue 2 will be the helper queue used during push operation
        self.queue1 = deque()
        self.queue2 = deque()

    # Push element x onto the stack
    def push(self, x: int) -> None:
        # ToDo: Write Your Code Here.
        # check if self.queue1 is full
        # use a loop to push all elements from queue2 to queue1
        self.queue2.append(x)
        while self.queue1:
            self.queue1.append(self.queue2.pop(0))
        
        self.queue1, self.queue2 = self.queue2, self.queue1

    # Pop element from the stack
    def pop(self) -> int:
        # ToDo: Write Your Code Here.
        # check if queue1 is empty
        # remove the first element from queue1
        return 0

    # Get the top element
    def top(self) -> int:
         # ToDo: Write Your Code Here.
         # return index 0 of queue1
        return 0

    # Check if the stack is empty
    def empty(self) -> bool:
        # ToDo: Write Your Code Here.
        return False
