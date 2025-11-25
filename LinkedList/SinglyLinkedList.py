class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertion(self, data): 
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        # points tail to the new node
        self.tail.next = new_node
        # assigns tail to the new node
        self.tail = new_node

    def delete(self, data):
        """
        Removes an element will be removed from the LinkedList
        Args: data that will be removed
        """
        # 1) if first node head None; return False
        if self.head is None:
            return False
        
        # 2) if first node == data; assigns first node to the node after
        if self.head.data == data:
            self.head = self.head.next
            print(f"New Head: {self.head.data}")
            if self.head is None:
                self.tail = None
            return True
        
        # 4) if deleting middle node or tail 
        current = self.head
        while current.next:
            if current.next.data == data:
                # Special Case: when current node has reached the tail
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                return True
            current = current.next # continue to traverse

        return False 
    
    def deleteAtPosition(self, index):
        #1) checks if the head is empty; if empty, return false
        if self.head is None:
            return False
        
        #2) head detection case at position 0
        if index == 0:
            self.head = self.head.next
            return

        #2) traverse through the linkedlist; if the position matches index
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        if current.next == self.tail:
            self.tail = current

        if current.next is not None:
            current.next = current.next.next
    
    def reverseList(self):
        """Reverse a LinkedList"""
        prev, current = None, self.head
        
        while current:
            # temporarily stores the next node so we don't lose access 
            nxt = current.next
            # make the node after point to previous node
            current.next = prev
            # move previous node forward
            prev = current
            # move current forward to next node
            current = nxt
            
            # 1) temp store the next node
            # 2) make the next node point to the previous
            # 3) move previous node forward
            # 4) point current to the next value
        return prev

    def remove_duplicate(self):
        """Removes duplicates from a Sorted List"""
        pass
    
    def merge_two_list(self):
        pass

    def traverse(self):
        current = self.head
        while current:
            current = current.next
    
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        return print("NULL")

if __name__ == '__main__':
    s = SinglyLinkedList()
    s.insertion(1)
    s.insertion(2)
    s.insertion(3)
    s.insertion(4)
    s.display()
    s.deleteAtPosition(5)
    s.display()