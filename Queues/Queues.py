class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queues:
    def __init__(self):
        #Linked List based Queue. Therefore, its dynamic
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        """
        Adds element to the end
        Args: a data that will be added to the Queue
        """
        new_node = Node(data)
        # checks if Queue is full
        if self.front is None:
            self.front = new_node
            self.rear = new_node
            self.size += 1
        # set the rear to the position after
        self.rear.next = new_node
        # update the rear pointer to the new node 
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        """
        Removes an element from the front of the Queue
        """
        if self.front is None:
            return None
        # create a temp var to store the pointer
        temp = self.front
        # this points front to the next node
        self.front = temp.next

        if self.front is None:
            self.rear = None
        self.size -= 1
        return temp.data

    def peak(self):
        """Returns the data from the front node without removing it"""
        if self.front is None:
            return None
        return self

    def reverse(self):
        if self.front is None:
            return None
        
        self.stack = []
        current = self.front
        while current:
            self.stack.append(current.data)
            current = current.next

        current = self.front
        while self.stack:
            current.data = self.stack.pop()
            # print(f"Current data: {current.data}")
            current = current.next
        return 

    def traverse(self):
        current = self.front
        while current:
            yield current
            current = current.next
    
    def display(self):
        current = self.front
        while current:
            print(current.data)
            current = current.next

if __name__ == '__main__':
    q = Queues()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.reverse()
    q.display()