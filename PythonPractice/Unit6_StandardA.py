# Unit 6 Standard A
# 4


from ast import List
from email import headerregistry
from os import link


class Node:
	def __init__(self, value, next_node=None):
		self.value = value
		self.next = next_node

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def mystery_function(head):
    if head is None:
        return None

    if head.next is None:
        return None

    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head

head = Node(1, Node(2, Node(3)))

print_linked_list(mystery_function(head))

# 6
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

# 7 debug: count_nodes_with_value() accepts the head of a singly linked list and a value, and returns the number of nodes in the linked list with value value.
# Complete the 'count_nodes_with_value' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER val
#
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


# 1 
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_ARRAY values as parameter.

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

def create_linked_list(values):
    linked_list = SinglyLinkedList()
    for value in values:
        linked_list.insert_node(value)
    return linked_list.head

values = [1,2,3,4]
#print_linked_list(create_linked_list(values))

# 2 insert node into list
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER value
#  3. INTEGER position

# For your reference:
#
# ListNode:
#     int val
#     ListNode next

# class Node:
#     def __init__(self, val=None):
#         self.val = val
#         self.next = None

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def insert_node(self, val):
#         node = ListNode(val)

#         if not self.head:
#             self.head = node
#         else:
#             self.tail.next = node

#         self.tail = node

# def print_linked_list(head):
#     current = head
#     while current:
#         if current.next:
#             sys.stdout.write(str(current.val) + " -> ")
#         else:
#             sys.stdout.write(str(current.val) + "\n")
#         current = current.next


#
# Complete the 'insert' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER value
#  3. INTEGER position
#

#
# For your reference:
#
# ListNode:
#     int val
#     ListNode next
