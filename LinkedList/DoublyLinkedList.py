class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def Delete(self, data, index):
        new_node = Node(data)

        # 1) Special Case: Deleteing in the beggining
        if index == 0:
            # tells program that what's after self.head
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            return
        
        # 2) Find the node at (index - 1)
        prev = self.head
        for _ in range(index - 1):
            if prev is None:
                print(f"index {index} is invalid")
                return
            prev = prev.next

        # 3) Bounds check after iteration
        if prev is None:
            print(f"Invalid index")
            return

        # 4) Assigns next node as new_node
        # sets new_node.next to point to the node after prev so new_node fits between prev and prev.next
        new_node.next = prev.next
        # this tells the node after that the the node before is now new_node
        if prev.next is not None:
            prev.next.prev = new_node
        # prev points forward to the new_node
        prev.next = new_node
        # assigns the node to new_node
        new_node.prev = prev
    
    def delete_at_index(self, index):
        if self.head is None or index < 0:
            return False
        
        current = self.head
        pos = 0

        while current:
            if pos == index:
                if current.prev is None and current.next is None:
                    self.head = None
                    self.tail = None
                    return True

                # Delete at head
                if current.prev is None:
                    self.head = current.next
                    self.head.prev = None
                
                # Delete at tail
                if current.next is None:
                    self.tail = current.prev
                    self.tail.next = None
                
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                
                return True
            
            pos += 1
            current = current.next

        return False

    def _forward(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print("NULL")

    def _reverse(self):
        if self.head is None:
            print(f"List is empty")
            return 
        current = self.head
        while current:
            current = current.next

        while current:
            print(current.data)
            current = current.prev
        print("NULL")

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.Delete(1)
    dll.Delete(2)
    dll.Delete(3)
    dll.Delete(4)
    dll._forward()