"""
Problem 1: Remove Duplicates from Sorted List 

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

Constraints
- The number of nodes in the list is in the range `[0, 300]`.
- `-100 <= Node.val <= 100`
- The list is guaranteed to be **sorted** in ascending order.
"""

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#       self.val = val
#       self.next = next
#
# Your function deleteDuplicates is called as such:
# head = ListNode(1)
# head.next = ListNode(1)
# deleteDuplicates(head)

class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next
      
def deleteDuplicates(head: ListNode) -> ListNode:
    current = head
    while current and current.next:
       if current.val == current.next.val:
          current.next = current.next.next
       else:
          current = current.next
    return head

# Function to print the linked list with a label
def print_list(label, node):
   print(label, end=": ")
   while node:
      print(node.val, end=" -> " if node.next else "\n")
      node = node.next

# Example 1 usage:
head1 = ListNode(1)
head1.next = ListNode(1)
head1.next.next = ListNode(2)
new_head1 = deleteDuplicates(head1)

print_list("Example 1", new_head1)

# Example 2 usage:
head2 = ListNode(1)
head2.next = ListNode(1)
head2.next.next = ListNode(2)
head2.next.next.next = ListNode(3)
head2.next.next.next.next = ListNode(3)
new_head2 = deleteDuplicates(head2)
     
print_list("Example 2", new_head2)

"""
Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""