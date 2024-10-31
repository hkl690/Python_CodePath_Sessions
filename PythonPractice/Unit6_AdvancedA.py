# 4
class SinglyLinkedListNode:
	def __init__(self, node_data, next_node=None):
		self.data = node_data
		self.next = next_node

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.data, end=" -> " if current.next else "")
        current = current.next
    print()

def mystery_function(head):
    if not head or not head.next:
        return head

    prev = None
    tail = head
    while tail.next:
        prev = tail
        tail = tail.next

    if not prev:
        return head

    tail.next = head.next
    prev.next = head
    head.next = None

    return tail

head = SinglyLinkedListNode(1, SinglyLinkedListNode(2, SinglyLinkedListNode(3, SinglyLinkedListNode(4, SinglyLinkedListNode(5)))))
print_linked_list(mystery_function(head))

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)



# 7 find the Bug
# Complete the 'count_nodes_with_value' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER val

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

def count_nodes_with_value(head, val):
    count = 0
    current = head

    while current: 
        if current.data == val:  
            count += 1
        current = current.next

    return count

# 1 reverse between
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, val):
        node = ListNode(val)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

# Helper function to print linked list (for testing)
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

#
# Complete the 'reverse_between' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER left
#  3. INTEGER right

# For your reference:
#
# ListNode:
#     int value
#     ListNode next

def reverse_between(head, left, right):
    if not head:
        return None
    temp = ListNode(0)
    temp.next = head
    prev = temp

    for _ in range(left - 1):
        prev = prev.next

    start = prev.next
    then = start.next

    for _ in range(right - left):
        start.next = then.next
        then.next = prev.next
        prev.next = then
        then = start.next

    return temp.next

# Creating linked list for testing
linked_list = SinglyLinkedList()
for val in [1, 2, 3, 4, 5]:
    linked_list.insert_node(val)

# Reversing between positions 2 and 4
reversed_list = reverse_between(linked_list.head, 2, 4)
print_linked_list(reversed_list)      

# Unit 6 Advanced B
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

def mystery_function(head_a, head_b):
    if head_a is None or head_b is None:
        return head_b, head_a
    head_a.next, head_b.next = head_b.next, head_a.next
    return head_b, head_a

# Helper function to print linked list (for testing)
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Creating linked lists for testing
head_a = Node(1, Node(2, Node(3)))
head_b = Node(4, Node(5, Node(6)))

# Swapping the heads
new_head_a, new_head_b = mystery_function(head_a, head_b)

# Printing the results
print("List A after swap:")
print_linked_list(new_head_a)
print("List B after swap:")
print_linked_list(new_head_b)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, val):
        node = ListNode(val)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
 

# 1
# Complete the 'has_cycle' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.

# For your reference:
#
# ListNode:
#     int value
#     ListNode next

def has_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False