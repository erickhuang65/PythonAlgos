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

**Types of Data Structures**

Primitive Data Structures:
- integer
- float
- character
- boolean

Non-Primitive Data Structure:

1. Linear:
Direct Access Linear DS
- Array

Sequential Access Linear DS
- Linked List
- Stack
- Queue

2. Non-Linear:

Hiearchical Non-Linear DS
- Trees (Binary Tree, BST, AVL, etc..)
- Heaps (special type of tree)
- Trie (special type of tree)

Unordered Non-Linear DS
- Matrix (2D array - grid structure)
- Graphs
- Sets
- Hash Tables

**Big-O notation**
- mathematcial notation that is used to describe the performance or complexity of an algorithm; how long an algorithm takes to run as the input size grows
- it provides a rough estimate of how long an algorithm takes to run (how much memory it uses), based on the size of the input
- provides a way to compare running time of different algos, regardless of specific hardware or implementation
- only provides upper bound on the running time of an algorithm

Time Complexity
- meaures how long an algo takes to run based on input size

Space Complexity
- measure how much memory an algo requires based on the size of input

Examples of Time Complexity:

1. O(1): Constant Time; running time is independent of the size of input
2. O(n): Linear Time; running time increases linearly with the size of input
3. O(n^2): Quadratic Time; running time increases is proportional to the square of the size of the input
4. O(logn): Logarithmic Time; running time increases logarithmically with the size of the input
5. O(2^n): Exponential Time; running time increases exponentially in the size of input

===========================================

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

===========================================

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

===========================================

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

======================================

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

===========================================

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

===========================================

**Tree & Binary Search Tree**

Tree Basics:
- is a hierarchical data structure that simulates a tree-like structure with a set of connected nodes
- unliked linear data structure (e.g., arrays or LinkedList), tree allows for more complex relationships and efficient organization of data
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
1. Inorder Traversal: Left subtree -> Root -> Right subtree
2. Preorder Traversal: Root -> Left subtree -> Right subtree
3. Postorder Traversal: Left subtree -> Right subtree -> Root

BST Limitation:
1. Unbalanced BST:
- tree could degenereate into a LinkedList if elements are inserted in a sorted or nearly sorted order
- leads to poor time complexity for searching, insertion and deletion, becoming closer to linear time instead of optimial logarithmic time

2. Degenerate Trees:
- extreme case of unbalanced BSTs where each node has only one child essentially forming a LinkedList
- results very poor time complexity for all operations, rendering the advantages of using BST ineffectively
- e.g., 4,3,2,1

3. Performance issue:
- unbalanced BST and degenerate Trees degrades common operations: search, insert, delete and can take linear time 

4. Complex Balancing:
- adds overhead and complexity to the code

5. Lack of Unique Keys:
- BST generally do not support DUPLICATED keys

6. Memory Overhead:
- each node in BST requires additional memory for storing pointers to the left and right children
- memory overhead can become significant for large datasets, especially if the tree is poorly balanced 

7. Not suitable for Dynamic Datasets:
- BST is not suited-well for frequently change in size
- Insertion and deletion could lead to imbalanced trees, requiring addiitonal balancing operations, which can be computationally expensive

8. Limited Search Performance for Equal Keys:
- BST provide efficient search time for unique keys, searching for the next greater or lesser element for equal keys requires addtional operation

===========================================

**Hash Tables**
- key-value pairs
- allow fast lookups, insertions, deletions
- efficiently managing retrieving data

*4 Main elements to any Hash Table*

Keys: unique identifier. Keys are inputs we feed into our hash function. It can be any data type - numbers, strings, or even objects. The crucial characteristics of keys is that they should be unique. If two pieces of data share the same key, it might lead to complications, like collisions

Values or Data: Values are the actual data stored in the Hash Table. Can be single number to a complex objects or even a function.

Hash Function: is the engine that drives a hash table. It is responsible for transforming keys into hash values, which dictate where we store our data in the table

Buckets: Think of bucket as shelves in our library, each one design to store a specific book or piece of data

*Basic Operations for Hash Tables*

Insert(key, value) - calculates hash index, stores the key-value pair in the slot at that index

Search(key) - finds the slot and returns the value associated with key, or null if not present

Delete(key) - removes key-value pair stored at index

Collisions 
- it occurs when an INSERT() tries to insert an item at a table slot already occupied by another item. 

Overflows
- occurs when the number of elements inserted exceeds fixed capacity allocated for the bucket array

Resolving Collisions
1. Open addressing/ Closed hashing
2. Chaining/ Open hashing

*Open Addressing (Closed Hashing)*

Open Addressing Techniques resolve hash collisions by probing the next available slot within the hash table itself. 

Collision Resolution Schemes:

1. Linear probing: simplest way to handle collisions by linearly searching consecutive slots for the next empty location

2. Quadratic probing: attemps to find an alternative empty slot for th ekey by using a quadratic funtion to probe the successive possible positions

3. Double hashing: uses two hash functions to determine the next probing location

4. Random probing: uses pseudo-random generator (PRNG) to compute the step size or increment value for probes in cases of collisions

*Separate Chaining (Open Hashing)*

Selects the right closed hashing technique for solving collisions can be tough; we'd need to keep the pros and cons of different strategies in mind and then make the best decision. 

Separate chaining offers simpler chaining mechanism to resolve collisions. Each slot in the hash table points to a separate data structure, such as linkedlist. This linkedlist or chain stores multiple elements that share the same hash index.

Separate chaining is an "open hashing" technique because hash table is "open" to accomodate multiple elements within a single bucket to handle collisions. 

Insertion in Separate chaining
- item with hash key (x), we could just append the item at the list/ chain linked in to x slot of the table. 

Deletion in Separate chaining
- do not need to keep any deletion sign or marks. Can directly delete the item's node from the chain linked to the relevant hash table slot

Perks of separate chaining
1. Dynamic Memeory Usage: Insertions appends new node at the chains. Therefore, the table with separate chaining can grow and shrink as per number of elements

2. Simple Implementation: using linked lists to manage collisions

3. Graceful Handling of Duplicates: allowing multiple records with the same key to be stored and retrieved accurately; 

Downside of separate chaining
1. Increased memory overhead: requires additional memory to store pointers or reference to linked lists for each bucket

2. Cache Inefficiency: because it resolves linked list, cache performance can be negatively impacted due to non-contiguous memory access

3. Dynamic allocation of memory for linked list can lead to external fragmentation, which may affect the performance of memory management in the system

4. Worst-Case Time Complexity: When multiple keys are hashed to the same bucket and form long linked lists, time complexity for search, insert, and delete can degrade to O(n)

5. Memory Allocation Overhead: Dynamic memory allocaiton for reach new element can add overhead and might lead to performance issues when the system is under high memory pressure

*Selecting Hash Function*
Characteristics of a good hash function:

1. Hash function should spread out keys evenly across all slots in hash table. Each slot should have equal chance of being hashed to. 
2. Efficient; requires minimal processing power and time to compute
3. Different keys should end up getting mapped to different slots as much as possible. 

Divison Method: Calculating the remainder obtained by dividing the key by the size of the hash table. The remainder is taken as the hash code (hash_key = key % table_size). However, if table size is not a prime number, it may lead to clustering. 

Folding Method: Dividing the key into smaller parts and then combining them to calculate the hash code. It is useful when dealing with large keys or when key does not evenly fit into the hash table size. 

Digit sum: hash_key = (5+3+2+4+6+1)%5 = 21%5 = 1

Reduction: hash_key = ()

Mid-square Method: 

===========================================

**HashSets**
- collection of unique elements where duplicates are not allowed

Hash Characteristics: 
- ensures every element is unique
- allows ONLY one null value
- HashSets do not maintain a specific order

HashTable vs HashSet:
- HashTable is like a dictionary, where key is associated iwth a value
- HashSet is like a unique-word collector - it doesn't care about meanings, just that word

**When to use HashSet**
- fast lookups; check if an element exist is O(1)
- remove duplicates
- unordered collections - when order does not matter
- unique storage - best for storing distinct items

Time Complexity of HashSet
- Insertion, LookUp, Deletion typically runs O(1) time because hash function computes an index directly
- Worst case, operations degrades to O(n) if multiple elements collide and are stored in a single bucket, requiring linear search
- HashSet performs efficiently as long as collisions are minimized and load factor is maintained

Space Complexity of HashSet
- HashSets requires O(n) space in an average case, where n is the number of stored elements
- if resizing occurs due to high load factor, temporary space usage may increase to O(n+m), where m is the new table size after rehashing

===========================================

**Heap**
- Tree-based data structure 
- Designed for efficient priority management
- Widely used in priority queues, Dijkstra's shortest path algorithm, heap sort
- It is a special type of binary tree that maintains a specific order between parent and child nodes
- It is always a complete binary tree

*Two types of Heaps*
1. Max Heap: every parent node has a value greater than or equal to it's children, ensuring largest element is at the root
2. Min Heap: every parent node has a value smaller than or equal to its children, ensuring smallest element is at the root

Unlike Binary Search Tree, Heaps does not enforce an ordering between siblings and only between parents and children. To optimize performance, heaps are commonly stored as arrays, making operations like insertion, deletion, and retrieval very efficent


