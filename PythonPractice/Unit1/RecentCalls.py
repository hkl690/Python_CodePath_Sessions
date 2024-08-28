"""
Problem 3: Number of Recent Calls
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.
"""

# RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

from collections import deque

class RecentCounter:
    
    def __init__(self):
        # Create a new double-ended queue
        self.queue = deque()
        
    def ping(self, t: int) -> int:
        # Upon Ping add new ping to queue
        self.queue.append(t)
        print(f"After appending {t}: {list(self.queue)}")  # Print the queue after appending
        # print(f"After appending {t}: {self.queue}") printing the deque without casting list
        # Another way to print the same thing: print("After appending " + str(t) + ": " + str(self.queue))
        
        # Remove all ping in queue with value more than 3000 away from new ping
        while self.queue and self.queue[0] + 3000 < t:
            removed = self.queue.popleft()
            print(f"Removed {removed}: {list(self.queue)}")  # Print the queue after removing
        
        print(f"Final queue: {list(self.queue)}")  # Print the final state of the queue
        return len(self.queue)

# Test the RecentCounter class
def test_recent_counter():
    recentCounter = RecentCounter()
    
    print(f"Recent count after ping 1: {recentCounter.ping(1)}\n")    # Expected output: 1
    print(f"Recent count after ping 100: {recentCounter.ping(100)}\n")  # Expected output: 2
    print(f"Recent count after ping 3001: {recentCounter.ping(3001)}\n") # Expected output: 3
    print(f"Recent count after ping 3002: {recentCounter.ping(3002)}\n") # Expected output: 3
    
# Run the test
test_recent_counter()    

"""
Example 1:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
"""