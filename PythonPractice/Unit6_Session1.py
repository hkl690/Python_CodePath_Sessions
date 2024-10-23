# Problem 1: Building a Playlist
# The assignment statement to the top_hits_2010s variable below creates the linked list Uptown Funk -> Party Rock Anthem -> Bad Romance. Break apart the assignment statement into multiple lines with one call to the Node constructor per line to recreate the list.

class SongNode:
	def __init__(self, song, next=None):
		self.song = song
		self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()
		
# top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))

node3 = SongNode("Bad Romance")
node2 = SongNode("Party Rock Anthem", node3)
top_hits_2010s = SongNode("Uptown Funk", node2)

# Example Usage:

print_linked_list(top_hits_2010s)
# Example Output: Uptown Funk -> Party Rock Anthem -> Bad Romance

# 💡 Hint: Nested Constructors
# This problem requires you to be familiar with nesting constructors. The Node class below accepts two parameters:

# the value of the Node object.
# the next Node object in the linked list or None if the Node is not linked to another node.
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
# In the past, we constructed each node in the list individually, then linked them together.

node_one = Node(1)
node_two = Node(2)
node_one.next = node_two
# We can instead chain together our constructor calls, and pass in a second Node object Node(2) as the next argument for the first node.

head = Node(1, Node(2))
# This technique is commonly used when generating test cases for linked lists.

# Problem 2: Top Artists
# Given the head of a linked list playlist, return a dictionary that maps each artist in the list to its frequency.

# Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):    
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

def get_artist_frequency(playlist):
    if not playlist:
        return {}
    artist_frequency = {}
    current = playlist
    
    while current:
        if current.artist in artist_frequency:
            artist_frequency[current.artist] += 1
        else:
            artist_frequency[current.artist] = 1
        current = current.next
    return artist_frequency

# Example Usage:

playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

print(get_artist_frequency(playlist))
# Example Output: { "SZA": 2, "Jimin" : 1, "Sabrina Carpenter": 1}