"""
Problem 2: Linked List Cycle
 
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again 
by continuously following the next pointer. Internally, pos is used to denote the index of 
the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Understanding "pos is not passed as a parameter." When solving the problem programmatically, 
the pos is not an input to your function. It is used only to describe the setup of the linked list. 
Your function will only take the head of the linked list as input, and you need to determine 
if there is a cycle without any additional information about pos.
"""

class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val    # value stored in the node
      self.next = next  # reference to the next node in the list
      
def hasCycle(head: ListNode) -> bool:
    current = head
    while current and current.next:
       