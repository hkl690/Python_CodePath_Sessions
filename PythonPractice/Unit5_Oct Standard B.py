# 4 find the bug

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

def print_singly_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "\n")
        current = current.next
#
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

# Test the function
list1 = SinglyLinkedList()
list1.insert_node(1)
list1.insert_node(2)
list1.insert_node(2)
list1.insert_node(3)
list1.insert_node(2)

print_singly_linked_list(list1.head)  # Output: 1 -> 2 -> 2 -> 3 -> 2
print(count_nodes_with_value(list1.head, 2))  # Output: 3


# 1 linked list traversal: return a list of the values in the linked list in the order they appear
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

def print_singly_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "\n")
        current = current.next


# Complete the 'traverse_linked_list' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

def traverse_linked_list(head):
    lst = []
    current = head

    while current:
        lst.append(current.data)
        current = current.next
    return lst

# Test the function
list1 = SinglyLinkedList()
list1.insert_node(1)
list1.insert_node(2)
list1.insert_node(3)
list1.insert_node(4)
list1.insert_node(5)

print_singly_linked_list(list1.head)  # Output: 1 -> 2 -> 3 -> 4 -> 5
print(traverse_linked_list(list1.head))  # Output: [1, 2, 3, 4, 5]

# 2 Linked list delete: delete the first occurrence of a node with a given value in the linked list. The function should return the head of the updated linked list. If no node with the given value exists, return the head of the original linked list.

def delete_node(head, value):
    current = head
    prev = None

    if not head:
        return head

    if head.data == value:
        return head.next

    while current:
        if current.data == value:
            if prev:
                prev.next = current.next
            return head
        prev = current
        current = current.next

    return head

# 3 Find occurrence: given the tail of a 0-indexed doubly linked list and a value "value", implement a function that returns the smallest index of a node with value "value" in the given list. If no node with value "value" exists, return -1.

#!/bin/python
import math
import os
import random
import re
import sys

# Complete the 'find_smallest_index' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. Node tail
#  2. int val
#
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

def find_smallest_index(tail, val): # this function passes 5/10 cases
    # Write your code here
    current = tail
    index = 0
    smallest_index = -1
    
    while current:
        if current.val == val:
            if smallest_index == -1 or index < smallest_index:
                smallest_index = index       
        current = current.prev
        index += 1
        
    return smallest_index

# Create a doubly linked list: 1 <-> 2 <-> 3 <-> 2 <-> 1
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(2)
node5 = Node(1)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4

# Find the smallest index of value 2
print(find_smallest_index(node5, 2))  # Output: 1

