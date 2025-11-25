Grokking Data Structures & Algorithms for Coding Interviews:

Key Considerations for Arrays in Coding Interviews:

Validate Assumptions:
Duplicates: Ask if duplicates are allowed
Sorted/ Unsorted Array: Some algorithms (e.g. binary search) required sorted arrays

Handle Boundaries: 
Index Out of Bounds:Always check valid indices to avoid errors
Negative indices: In Python, negative indices access elements from the end

Efficiency Considerations: 
Slicing and Concatenation: Takes O(n) time, avoid unnecessary operations
In-place vs. Extra space: Try to optimize space usage

Loops & Naming: 
Use description variable names: improve code clarity
Watch Loop Indices: Avoid off-by-one errors

Algorithm Choice: 
Time & Space Complexity
Nested Loops: Avoid if possible, as they increase time complexity

Testing & Edges Cases: 
Empty, Single-element, large arrays: always test edge cases
Various inputs: ensure the solution work for all possible cases

Handling Special Values: 
Zero & Negative Numbers: important for sum/ product-based problems

Modifying While iterating: 
Avoid direct modification: use a copy or iterate backward if needed

Array Methods: 
Know Built-in Methods: understand their time complexity


**ARRAY**:
- collection of items stored in single block of memeory
- Index-Based Access
- Fixed Position in Memory

Array offers simple way to store many similar values using one identifier
Array store elements in a contiguous memory locations. This allow fast access

Static Arrays: fixed size that is defined when created; remains unchanged 
Dynamic Arrays: size can change at runtime; added, removed as needed

Brute Force:
- Compare each element with other elements in the array

Hash Set:
- set data structure to store unique values


**MATRIX**:
- two-dimensional data structures used for storing elements in a grid-like format with rows and columns
- commonly used in graph problems, dynamic programming, image processing, pathfinding algorithms, game development

Matrices are Important in DSA 
- Efficient representation
- it uses row and column indices so accessing element is O(1)
- useful for algorithms; flood fill, shortest path (BFS/ DFS) and adjacency matrices
- memory efficiency, improving cache performances

Accessing Matrices:
df[row][column]
df[0][0] = (first row, first column)


**STACK**:
- its a linear data structure that follows "Last-in, First-out" (LIFO) principal
- Array based stacks are simple but have fixed size
- Linked-list-based stacks provide dynamic memory but require extra space for pointers
- Both are O(1)
- In Python, Stack is implemented through a list

Stack Operations:
- Append()
- Pop(index)
- Peek (or Top)
- isEmpty
- isFull
- reversed() - returns a reverse iterator

Append:
- Time Complexity: O(1)
- Space Complexity: O(1)

Pop:
- Time Complexity: O(1)
- Space Complexity: O(1)

isEmpty:
- if Stacks have no element, return True
- else, return False
- Time Complexity: O(1)
- Space Complexity: O(1)

Stacks are widely used in Comp Sci and real-world applications because of LIFO. Efficient solutions, involving reversibility, function calls, data backtracking

1. Memory Management (Function Call Stack)
Manages function calls in programming by pushing function calls onto the stack and popping them after execution.
Enables recursion, where each function call gets a new stack frame.
Helps in tracking local variables and return addresses for each function.

2. Expression Evaluation & Syntax Parsing
Ensures correct execution order in arithmetic expressions by managing operator precedence.
Used in parsing programming languages, particularly for validating brackets and expressions.
Converts infix expressions to postfix notation, which is easier for computers to evaluate.
3. Undo/Redo Mechanism in Software
Stores user actions as stack operations in text editors, image editors, and IDEs.
Pressing Undo pops the last action from the stack and reverses it.
Redo re-applies an action by pushing it back onto the stack.

4. Backtracking Algorithms
Used in problems that require trying different possibilities and reverting if needed.
Common in Sudoku solvers, maze pathfinding, and the N-Queens problem.
Stores previous states, allowing the algorithm to revert to an earlier position when a dead end is reached.

5. Depth-First Search (DFS) in Graphs
DFS explores a graph deep into one path before backtracking.
Uses a stack to store nodes that need to be visited.
Helps in finding connected components, cycle detection, and solving maze problems.

6. Web Page History (Back Button in Browsers)
Every visited web page is pushed onto the history stack.
Clicking "Back" pops the last visited page, returning the user to the previous one.
This method allows users to navigate webpages in reverse order efficiently.


**Queue**:
- FIFO (First-In-First-Out)
- IMPLEMENT with LinkedList (Node) DataStructure

**Queue Terms:**
- Enqueue: add an element at the end
- Dequeue: removes an element from the front

Enqueue:
- adds an elements at the end
- edge case: how do we know if we can add more element to the end of the line?
- BEFORE ADDING: we must check if Queue is FULL
- ALWAYS CHECK FOR QUEUE OVERFLOW OR UNDERFLOW conditions

Dequeue:
- removes an element from the front
- edge case: BEFORE removing, we must check if there are any items to remove

Operations:
- Peek() and isEmpty() operations
- Peek(): let's us see if first element in the Queue
- isEmpty(): let's us know if Queue is empty

Imeplementation:
- Each Node structure represents each element of the Queue
- Each Node will have a variable to store the data and Node pointer which will be pointing to the next element
- In Queue class, we have two pointers; one to the front of Node of the Queue., and one to the rear Node
- Each Node contains DATA and REFERENCE to the next node in the list

Class Attributes:
- front: reference to the first node in Queue
- rear referernece to the rear node in Queue
- size: an integer tracking the number of elements in the Queue

Constructor:
- initializes an empty queue where front and rear are set to null and size is set to 0

Enqueue Implementation:
- new node is created with given data
- if Queue is empty (rear == null), both front and rear points to the new node
- if queue is not empty, the new node is added after rear, and then rear is updated to point to the new node
- size of queue is incremented

Dequeue Implementation:
- if queue is empty (front == null), method returns null
- the front node is saved
- front is updated to point to the next node in the queue
- if queue becomes empty after this operation (front == null), ear is also set to null
- returns the saved data

Peek Imlementation:
- returns the data from the front node without removing it
- if queue is empty (front == null), it returns null
- otherwise, return the data fron the front node

Utility methods:
- isEmpty(): checks if queue is empty (i.e., size == 0)
- size: returns the number of elements in the Queue

Queue comes in different variations based on how elements are inserted, removed and prioritized

Simple Queue: most basic form of queue. Follows FIFO

Circular Queue: 
- last position is connected back to the first
- this eleminates the need for shifting elements
- simple queue can result in wasted space when elements are dequeued
- Dequeue (remove an element) from the front
- Enqueue (add an element) from the front

Priority Queue:
- every element has a priority and is enqueured based on that priority
- assigns priority to each element, and elements are dequeued based on their priority
- Higher priority elements are dequeued first, regardless of when they are enqueued
- can be implemented using heaps
- e.g., [(3, "Task A"), (1, "Task B"), (2, "Task C")]
- Not strictly FIFO 
- used in operating systems (processing schedules, networking), and Dijkstra's Algorithm

Afinity Queue:
- every element has an afinity & is placed with an element having the same afinity; otherwise placed at the rear
- if no matching affinity is found, the element is placed at the rear
- e.g., (multi-threading tasks)
- imporves cache locality and system efficiency
- used in thread scheduling, data processing and database transaction
- e.g., [(A, 10), (A, 15), (A, 20), (A, 30)]

Deque (Double-Ended Queue):
- allows insertion and deletion from both ends
- Front Insertion & Rear Insertion
- Front Removal & Rear Removal


**LinkedList**
- node is a building block of a LinkedList

Node contains:
- Data 
- Next Pointer

Head
- First node of a linked list and stores the reference to the first node

Tail
- last node of the linked list. 
- in Circular Linked List, it points back to the head

Null 
- last node of the singly linked list points to NULL; indicates the final node

**Singly LinkedList**
- each node contains data and pointer to the next node
- traveral is one-directional, can only move forward to through the list -> NULL
- the last node's pointer is NULL, indicating the end of the lis
- **efficient for sequential traversal and insertions at the beggigning**

**Doubly LinkedList**
- each node contains data, pointer to the next node, and a pointer to the previous node
- allows two way traversal
- **efficient deletion because of the two way traversal**
- requires extra memory due to the addtional pointer

**Circular LinkedList**
- last node points back to the first node, forming a loop
- can be singly or doubly circular
- NO NULL pointers; last node connects to the first
- Useful in buffered data structures e.g., audio/video streaming

OPERATIONS OF DIFFERENT LINKED LISTS:

Singly LinkedList
- Traversal (visiting each node sequentially)
- Insertion (adding a node at the beggining, middle or end)
- Deletion (removing a node from the beggining, middle or end)

Doubly LinkedList
- Traversal (visiting each node in sequence in two ways; forward, backward)
- Insertion (adding a new node at a specified position) adjusting both next and prev pointers (beggining, end position, or middle position)
- Deletion (removes a node while ensuring both next and prev pointers neighboring nodes are correctly updated; deletion can occur at beggining, end, and middle)


**Tree & Binary Search Tree**

Tree Basics:
- is a hierarchical data structure that simulates a tree-like structure with a set of connected nodes
- unliked linear data structure (e.g., arrays or LinkedList), tree allows for more complex relationships and efficient organizaiton of data
- useful for represeting data that forms a hierarchy (e.g., file systemms)
- made up of nodes that are arranged in hierarchical structure
- top hierarchy is root node - acts as the starting point
- the nodes are grouped into levels, and the maximum level of any node is the tree referred as depth

Terminology:
Root Node: 
- Node at top of the tree. It is the node from the whole tree originates

Nodes: 
- all elements in the tree, including the root; each node has an unique value, and may have child node

Parent Node:
- node that has 1 or more child node

Child Node:
- node that's directtly connected to a parent node

Ancestor Node:
- All nodes in the path from a specific node to the root node

Descendant Node:
- all nodes reachable from a specific node down to the leaves

Leaf Node:
- node in the tree that do not have any children

Internal Node:
- node with at least one child

Edge:
- the connection between on node to another

Path:
- sequence of nodes connected by edges

Height of a node:
- number of edges on the longest path from the node to a leaf

Depth of a node:
- the number of edges from the node to the tree's root node

Height of the tree:
- the sheight of the root node

Degree of a node:
- the number of children a node has

Subtree:
- a smaller tree within the main tree, consisting of a node and its desecedants

**Binary Tree:**
- type of tree where each node can have at most 2 children (left & right children)

**Full Tree:**
- every node has either 0 children (leaf node) or 2 children

**Complete Tree:**
- is a binary tree which all levels are filled, except possibly the last level
- the last level must stricly be filled from left to right
- Data Structures like Heap uses compelte tree

**Balanced Tree:**
- binary trees where the difference in height between the left and right subtrees of any node is not > 1

**Multi-way Tree:**
- allow nodes to have more than 2 children
- each node can have multiple branches, making mult-way trees more flexible representing hiearchical data

**Binary Search Tree (BST)**
- traversal refers to visitng each node in a specific order
- there are three main types of depth-first traversal techniques
