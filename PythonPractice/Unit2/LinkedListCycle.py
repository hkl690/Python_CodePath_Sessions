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
    # if the linked list is empty, just return False for no cycle
    if not head or not head.next:
        return False

    # Establish two points    
    slowPointer = fastPointer = head
    
    # if the linked list has a loop, the two pointers will meet,
    # otherwise one will eventually become none
    while fastPointer and fastPointer.next:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next # move fastPointer two steps
        
        if slowPointer == fastPointer:
            return True
        
    return False

def printLinkedList(head: ListNode):
    current = head
    visited = set()
    while current:
        if current in visited:    
            print(current.val, end=" -> ")
            print("(cycle detected)")
            return
        visited.add(current)
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Create the linked list nodes
node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

# Link the nodes together
node1.next = node2
node2.next = node3
node3.next = node4

# Create the cycle
node4.next = node2 # pos = 1 (0-indexed)

# Test the function
print("Example 1: ", hasCycle(node1)) # Expected Example 1 output: True
printLinkedList(node1)

node5 = ListNode(1)
node6 = ListNode(2)
node5.next = node6  # create the linked list
node6.next = node5  # create the cycle

print("Example 2: ", hasCycle(node5)) # Expected Example 2 output: True
printLinkedList(node5)

node7 = ListNode(1)
print("Example 3: ",hasCycle(node7)) # Expected Example 3 output: False
printLinkedList(node7)

"""
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""