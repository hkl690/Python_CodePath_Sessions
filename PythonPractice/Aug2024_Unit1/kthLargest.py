"""
Problem 2: Kth Largest Element in a Stream
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums): Initializes the object with the integer k and the stream of integers nums.
int add(int val): Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
"""

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

import heapq
from typing import List

class KthLargest:
    """
    A class to find the k-th largest element in a stream.

    Attributes:
    k (int): The k-th position.
    min_heap (List[int]): A min-heap to store the k largest elements.
    """

    def __init__(self, k: int, nums: List[int]):
        """
        Initializes the KthLargest class with the given k and a list of numbers.

        Parameters:
        k (int): The k-th position.
        nums (List[int]): A list of integers.
        """
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)  # Transform the list into a heap, in-place, in linear time.
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)  # Maintain the size of the heap to be at most k.

    def add(self, val: int) -> int:
        """
        Adds a new value to the stream and returns the k-th largest element.

        Parameters:
        val (int): The new value to be added.

        Returns:
        int: The k-th largest element in the stream.
        """
        heapq.heappush(self.min_heap, val)  # Add the new value to the heap.
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)  # Maintain the size of the heap to be at most k.
        return self.min_heap[0]  # The k-th largest element is the smallest element in the heap.
    
    
    # Example usage
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))  # Output: 4
print(kthLargest.add(10)) # Output: 5
print(kthLargest.add(9))  # Output: 8
print(kthLargest.add(4))  # Output: 8

# Example usage based on the provided input and output
commands = ["KthLargest", "add", "add", "add", "add", "add"]
values = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

# Initialize the KthLargest object
kthLargest = KthLargest(values[0][0], values[0][1])
output = [None]  # The first command is initialization, so output is None

# Execute the add commands and collect the results
for i in range(1, len(commands)):
    result = kthLargest.add(values[i][0])
    output.append(result)

print(output)  # Output should be [None, 4, 5, 5, 8, 8]