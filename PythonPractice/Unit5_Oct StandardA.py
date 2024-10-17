# 4 Standard A
from email.quoprimime import header_check
from tokenize import Single


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.pets_received = 0

    def receive_pet(self):
        self.pets_received += 1
        return f"{self.name} has received a pet!"

    def bark(self):
        return f"{self.name} says woof!"

dog1 = Dog("Buddy", "Poodle")
dog2 = Dog("Bella", "Labrador")

print(dog2.bark())
print(dog1.receive_pet())
print(dog1.receive_pet())
print(dog1.pets_received)
print(dog2.receive_pet())
print(dog2.pets_received)

# 5 What is the runtime complexity
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_last(head):
    if not head or not head.next:
        return None

    current = head
    while current.next and current.next.next:
        current = current.next
    current.next = None

    return head

head = ListNode('a')
head.next = ListNode('b')
head.next.next = ListNode('c')
head.next.next.next = ListNode('d')
new_head = delete_last(head)

# 6
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mystery_function(head):
    nums1 = []
    nums2 = []
    current = head
    while current:
        if current.val%2 == 0:
            nums1.append(str(current.val))
        else:
            nums2.append(str(current.val))
        current = current.next
    return " -> ".join(nums1 + nums2)

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(mystery_function(head))

# 7 find the bug: when implemented correctly, count_nodes_with_value() accepts the head of a singly linked list and a value, and returns the number of nodes in the linked list with [that] value value
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

def print_singly_linked_list(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

def count_nodes_with_value(head, val):
    count = 0
    current = head
    
    while current:
        if current.data == val:
            count += 1
        current = current.next

    return count



# Create a linked list: 1 -> 2 -> 3 -> 2 -> 4
head = SinglyLinkedListNode(1)
head.next = SinglyLinkedListNode(2)
head.next.next = SinglyLinkedListNode(3)
head.next.next.next = SinglyLinkedListNode(2)
head.next.next.next.next = SinglyLinkedListNode(4)

# Test the function
print(count_nodes_with_value(head, 2))  # Output should be 2
print(count_nodes_with_value(head, 5))  # Output should be 0
print(count_nodes_with_value(None, 2))  # Output should be 0

# 1 create a linked list

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Test the function
nums = [1, 2, 3, 4, 5]
head = create_linked_list(nums)
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

nums = []
head = create_linked_list(nums)
print(head)  # Should print None

# 2 Insert Node into List
#!/bin/python

import math
import os
import random
import re
import sys
from tarfile import LENGTH_NAME

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

def print_singly_linked_list(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

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
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insert(head, value, position):
    new_node = SinglyLinkedListNode(value)

    # if inserting at the head
    if position == 0:
        new_node.next = head
        return new_node

    current = head
    current_position = 0

    # traverse the list to find the position
    while current is not None and current_position < position - 1:
        current = current.next
        current_position += 1

    # insert the new node
    if current is not None:
        new_node.next = current.next
        current.next = new_node

    return head

# Create a linked list
llist = SinglyLinkedList()
for i in range(1, 6):
    llist.insert_node(i)

# Print the original list
print("Original list:")
print_singly_linked_list(llist.head)

# Insert a node with value 10 at position 2
llist.head = insert(llist.head, 10, 2)
print("After inserting 10 at position 2:")
print_singly_linked_list(llist.head)

# Insert a node with value 20 at position 0 (head)
llist.head = insert(llist.head, 20, 0)
print("After inserting 20 at position 0:")
print_singly_linked_list(llist.head)

# Insert a node with value 30 at the end
llist.head = insert(llist.head, 30, 7)
print("After inserting 30 at the end:")
print_singly_linked_list(llist.head)

# 3 Longer List: return the head of the linked list with the greatest length. If they have the same length, return the first list

def longer_list(head_a, head_b):
    def get_length(head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length

    length_a = get_length(head_a)
    length_b = get_length(head_b)

    if length_a >= length_b:
        return head_a
    else: 
        return head_b

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def create_linked_list(values):
    if not values:
        return None
    head = SinglyLinkedListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = SinglyLinkedListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
    # Test Case 1
head_a = create_linked_list([1, 2, 3])
head_b = create_linked_list([1, 2])
print("Test Case 1:")
print_linked_list(longer_list(head_a, head_b))  # Expected Output: 1 -> 2 -> 3 -> None

# Test Case 2
head_a = create_linked_list([1, 2, 3])
head_b = create_linked_list([4, 5, 6])
print("Test Case 2:")
print_linked_list(longer_list(head_a, head_b))  # Expected Output: 1 -> 2 -> 3 -> None

# Test Case 3
head_a = create_linked_list([1, 2, 3])
head_b = create_linked_list([])
print("Test Case 3:")
print_linked_list(longer_list(head_a, head_b))  # Expected Output: 1 -> 2 -> 3 -> None

# Test Case 4
head_a = create_linked_list([])
head_b = create_linked_list([])
print("Test Case 4:")
print_linked_list(longer_list(head_a, head_b))  # Expected Output: None

# Advanced A
class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

def mystery_function(head_a, head_b):
    if head_a is None or head_b is None:
        return head_b, head_a

    head_a.next, head_b.next = head_b.next, head_a.next
    return head_b, head_a


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

head_a = Node(1, Node(2, Node(3)))
head_b = Node(4, Node(5, Node(6)))
head_a, head_b = mystery_function(head_a, head_b)
# Print the linked lists
print("head_a:")
print_linked_list(head_a)
print("head_b:", end=" ")
print_linked_list(head_b)

# 7 debug
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

def print_singly_linked_list(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

def create_linked_list(values):
    if not values:
        return None
    head = SinglyLinkedListNode(values[0])
    current = head
    for value in values[1:]:
        new_node = SinglyLinkedListNode(value)
        current.next = new_node
        current = new_node
    return head

def format_linked_list(node):
    if node is None:
        return 'None'
    result = []
    while node:
        result.append(str(node.data))
        node = node.next
    return ' -> '.join(result)

# Test the create_linked_list function
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)
print(format_linked_list(head))  # Expected output: 1 -> 2 -> 3 -> 4 -> 5 -> None

values = []
head = create_linked_list(values)
print(format_linked_list(head))  # Expected output: None


# 3 palindrome linked list

#!/bin/python

import math
import os
import random
import re
import sys
import ast

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

# Helper function to print linked list (for testing)
def print_linked_list(head):
    current = head
    output = []
    while current:
        output.append(str(current.data))
        current = current.next
    print(" -> ".join(output))

# Complete the 'is_palindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.
#
# For your reference:#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

def is_palindrome(head):
    values = []
    current = head
    while current:
        values.append(current.data)
        current = current.next
    return values == values[::-1]

# Create a linked list: 1 -> 2 -> 3 -> 2 -> 1
linked_list = SinglyLinkedList()
linked_list.insert_node(1)
linked_list.insert_node(2)
linked_list.insert_node(3)
linked_list.insert_node(2)
linked_list.insert_node(1)

# Print the linked list
print_linked_list(linked_list.head)  # Output: 1 -> 2 -> 3 -> 2 -> 1

# Check if the linked list is a palindrome
print(is_palindrome(linked_list.head))  # Output: True


# 2 merge two sorted lists
#!/bin/python

import math
import os
import random
import re
import sys

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

# Helper function to print linked list (for testing)
def print_linked_list(head):
    if head is None:
        return []
    current = head
    output = []
    while current:
        output.append(current.data)
        current = current.next
    return output

# Complete the 'merge_two_lists' function below.
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST l1
#  2. INTEGER_SINGLY_LINKED_LIST l2

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

def merge_two_lists(l1, l2):
    merger = SinglyLinkedListNode(0)
    current = merger

    while l1 and l2:
        if l1.data < l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    if l2:
        current.next = l2

    return merger.next

# Test the merge_two_lists function
list1 = SinglyLinkedList()
list1.insert_node(1)
list1.insert_node(3)
list1.insert_node(5)

list2 = SinglyLinkedList()
list2.insert_node(2)
list2.insert_node(4)
list2.insert_node(6)

merged_head = merge_two_lists(list1.head, list2.head)
print(print_linked_list(merged_head))  # Expected output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

# 1 DOES NOT WORK

# Complete the 'remove_elements' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER val

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

# def remove_elements(head, val):
#     temp_head = SinglyLinkedListNode(0)  # Use a temporary head node with a dummy value
#     temp_head.next = head
#     current = temp_head

#     while current.next:
#         if current.next.data == val:
#             current.next = current.next.next
#         else:
#             current = current.next
#     return temp_head.next

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_item(head, item):
    if not head:
        return None

    if head.value == item:
        return head.next

    current = head
    while current.next and current.next.value != item:
        current = current.next
    if current.next:
        current.next = current.next.next

    return head

slingshot = Node("Slingshot")
peaches = Node("Peaches")
beetle = Node("Scarab Beetle")
slingshot.next = peaches
peaches.next = beetle

# Linked List: slingshot -> peaches -> beetle
print_linked_list(delete_item(slingshot, "Peaches"))

# Linked List: slingshot -> beetle
print_linked_list(delete_item(slingshot, "Triceratops Torso"))

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

def print_reverse(tail):
    current = tail
    while current:
        if current.prev:
            print(current.value, end=" ")
        else:
            print(current.value)
        current = current.prev

isabelle = Node("Isabelle")
kk_slider = Node("K.K. Slider")
saharah = Node("Saharah")
isabelle.next = kk_slider
kk_slider.next = saharah
saharah.prev = kk_slider
kk_slider.prev = isabelle

# Linked List: Isabelle <-> K.K. Slider <-> Saharah
print_reverse(saharah)
# Expected Output: "Saharah K.K. Slider Isabelle"

