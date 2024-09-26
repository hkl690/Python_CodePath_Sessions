
cereals = ['cheerios', 'fruity pebbles', 'cocoa puffs']
for count, cereal in enumerate(cereals, start=1):
  print(count, cereal)

# dictionary methods
d = {'a': 1, 'b':2, 'c': 3}
d['d'] = 4          # Adds a new key 'd' with value 4
print(d)            # Outputs: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d['a'] = 10
print(d)
print(d['a']) # direct access by key, or use the get() method next which is considered safer since it won't raise an error if none is found
print(d.get('z'))
print(d.get('c'))
print(d.get('z', 'Not Found'))
print(d.keys())
keys = d.keys()
print(keys)
print(d.values())
print(d.items()) # each key-value pair is represented as a tuple
print(d)

# Example 1: Retrieving Album Data 
albums = [
            ["Sabrina Carpenter", "Short n' Sweet"], 
            ["FKA Twigs", "Magdalene"],
            ["Elliot Smith", "Either/Or"]]

first_album = albums[0]
print(first_album) # Output: ["Sabrina Carpenter", "Short n' Sweet"]

# Example 2: Updating a Row in a Matrix
matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix[2] = [100, 200, 300]
print(matrix) # Output: [[1, 2, 3], [4, 5, 6], [100, 200, 300]]

fka_twigs = albums[1][0]
print(fka_twigs)

# Example 1: Nested Dictionaries
address_book = {
    "John Doe": {
        "phone": "555-1234",
        "email": "johndoe@example.com",
        "address": {
            "street": "123 Maple Street",
            "city": "Springfield",
            "state": "IL",
            "zip": "62701"
        }
    },
    "Jane Smith": {
        "phone": "555-5678",
        "email": "janesmith@example.com",
        "address": {
            "street": "456 Oak Avenue",
            "city": "Shelbyville",
            "state": "IL",
            "zip": "62565"
        }
    }
}

address_book["John Doe"]["email"]
john_email = address_book["John Doe"]["email"]
print(john_email) # Output: 'johndoe@example.com'
print(address_book)
print(address_book["John Doe"]["phone"])
# Example 2: List of Dictionaries
students = [
    {
        "name": "John Doe",
        "age": 16,
        "grade": "11th",
        "favorite_subject": "Math"
    },
    {
        "name": "Jane Smith",
        "age": 17,
        "grade": "12th",
        "favorite_subject": "English"
    },
    {
        "name": "Emily Johnson",
        "age": 16,
        "grade": "11th",
        "favorite_subject": "Biology"
    }
]

jane_age = students[1]["age"]
print(jane_age) # Output: 17

# Nested Loops
for i in range(1, 4):
    print("Outer loop incremented")
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")

numbers = [3, 5, 2]

# Outer for loop iterates over each number in the list
for num in numbers:
    print(f"Counting down from {num}:")
    
    # Inner while loop counts down from the current number to 0
    while num >= 0:
        print(num)
        num -= 1  # Decrement the number by 1 each time
    
    print("---")  # Separator to indicate moving to the next number

numbers = [3, 5, 2]
for num in numbers[::-1]:
    print(f"Counting down from {num}:")
    print(num)
    num -= 1  # Decrement the number by 1 each time    
    print("---")  # Separator to indicate moving to the next number

# list comprehension with dictionary
oxygen_levels = {"Command Module": 21, "Habitation Module": 20, "Laboratory Module": 19, "Airlock": 22, "Storage Bay": 18}
min_val = 19 
max_val = 22
# Output: ['Storage Bay']
keys_outside_range = [key for key, value in oxygen_levels.items() if value < min_val or value > max_val]
print(keys_outside_range)

# or filter with lambda does the same thing
# Find keys with values outside the specified range using filter and lambda
keys_outside_range = list(filter(lambda key: oxygen_levels[key] < min_val or oxygen_levels[key] > max_val, oxygen_levels))

print(keys_outside_range)  # Output: ['Storage Bay']

# Find keys with values within the specified range
keys_within_range = [key for key, value in oxygen_levels.items() if min_val <= value <= max_val]

print(keys_within_range)  # Output: ['Command Module', 'Habitation Module', 'Laboratory Module', 'Airlock']


# 5
word = "encourage"
char_count = {}
for char in word:
    if char not in char_count:
        char_count[char] = 1
    else:
        char_count[char] += 1
char_count['e'] += 2
print(char_count['e'])

bart = {"first name": "Bart", "last name": "Simpson", "age": "10", "hometown": "Springfield"}
print(bart["hometown"])
print(bart.get("hometown"))
print(bart.pop("hometown"))

def mystery_function(old_dictionary):
    new_dictionary = {}

    for key, value in old_dictionary.items():
        new_dictionary[value] = key
    return new_dictionary

old_dictionary = {'a': 1, 'b': 2, 'c': 3}
new_dictionary = mystery_function(old_dictionary)
print(new_dictionary)

# Complete the 'get_top_player' function
# It is expected to return a STRING

def get_top_player(dictionary):
    high_score = 0
    top_player = ""

    for name, score in dictionary.items():
        if score > high_score:
            high_score = score
            top_player = name

    return top_player

old_dictionary = {'c': 3, 'a': 1, 'b': 2}
print(get_top_player(old_dictionary))

# 1

def find_min_index_of_repeating(arr):
    if len(arr) == 0:
        return None

    seen = {}
    for i, value in enumerate(arr):
        if value in seen:
            return seen[value]
        seen[value] = i
    return None

arr = [10,21,22,33,44,55,33]
print(find_min_index_of_repeating(arr))


#
# Complete the 'intersection' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums1
#  2. INTEGER_ARRAY nums2
#

def intersection(nums1, nums2):
    # Write your code here
    if len(nums1) == 0 or len(nums2) == 0:
        return []
        
    set1 = set(nums1)
    set2 = set(nums2)
    
    intersection_set = set1.intersection(set2)
    
    return sorted(list(intersection_set))

# Example 1:
nums1 = [1,2,2,1] 
nums2 = [2,2]
print(intersection(nums1, nums2))
# Output: [2]

# Example 2:
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))
# Output: [9,4] <-- incorrect, is [4,9]

# Example 3: Both arrays are empty
nums1 = []
nums2 = []
print(intersection(nums1, nums2))  # Output: []

# Example 4: No intersection
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
print(intersection(nums1, nums2))  # Output: []

# Example 5: Single element intersection
nums1 = [1, 2, 3]
nums2 = [3, 4, 5]
print(intersection(nums1, nums2))  # Output: [3]

# Example 6: All elements intersection
nums1 = [1, 2, 3]
nums2 = [1, 2, 3]
print(intersection(nums1, nums2))  # Output: [1, 2, 3]

# Example 7: Different lengths
nums1 = [1, 2, 3, 4, 5]
nums2 = [2, 4]
print(intersection(nums1, nums2))  # Output: [2, 4]

# Example 8: Negative numbers
nums1 = [-1, -2, -3, 4]
nums2 = [-3, 4, 5]
print(intersection(nums1, nums2))  # Output: [-3, 4]



def roman_to_int(s: str) -> int:
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for char in reversed(s): # reversed is a built-in function, does the same as s[::-1]
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total

print(roman_to_int("III")) # 3
print(roman_to_int("LVIII")) # 58   <- IIIVL in reverse
print(roman_to_int("MCMXCIV")) # 1994   <-- VICXMCM in reverse
print(roman_to_int("IV")) #4
print(roman_to_int("XI")) #11

# Unit 2 Session 2 Standard B 
# 
# Problem 1: Filter Destinations
# You're planning an epic trip and have a dictionary of destinations mapped to their respective rating scores. Your goal is to visit only the best-rated destinations. Write a function that takes in a dictionary destinations and a rating_threshold as parameters. The function should iterate through the dictionary and remove all destinations that have a rating strictly below the rating_threshold. Return the updated dictionary.

def remove_low_rated_destinations(destinations, rating_threshold):
    keys_to_remove = [key for key, value in destinations.items() if value < rating_threshold]
    print(keys_to_remove)
    for key in keys_to_remove:
        destinations.pop(key)
    return destinations

destinations = {"Paris": 4.8, "Berlin": 3.5, "Addis Ababa": 4.9, "Moscow": 2.8}
destinations2 = {"Bogota": 4.8, "Kansas City": 3.9, "Tokyo": 4.5, "Sydney": 3.0}

print(remove_low_rated_destinations(destinations, 4.0)) # {"Paris": 4.8, "Addis Ababa": 4.9}
print(remove_low_rated_destinations(destinations2, 4.9)) # {}

# Problem 2: Unique Travel Souvenirs
# As a seasoned traveler, you've collected a variety of souvenirs from different destinations. You have an array of string souvenirs, where each string represents a type of souvenir. You want to know if the number of occurrences of each type of souvenir in your collection is unique.

# Write a function that takes in an array souvenirs and returns True if the number of occurrences of each value in the array is unique, or False otherwise.

def unique_souvenir_counts(souvenirs):
    # create a dictionary to count souvenirs
    count_dict = {}
    for souv in souvenirs:
        if souv in count_dict:
            count_dict[souv] += 1
        else:
            count_dict[souv] = 1

    # create a set to track the counts seen
    seen_counts = set()

    # check if the counts are unique
    for count in count_dict.values():
        if count in seen_counts:
            return False
        seen_counts.add(count)

    return True

souvenirs1 = ["keychain", "hat", "hat", "keychain", "keychain", "postcard"]
souvenirs2 = ["postcard", "postcard", "postcard", "postcard"]
souvenirs3 = ["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"]

print(unique_souvenir_counts(souvenirs1))  
print(unique_souvenir_counts(souvenirs2)) 
print(unique_souvenir_counts(souvenirs3))
# Expected Outputs:
# True
# Example 1 Explanation: The value "keychain" has 3 occurrences, "hat" has 2 
# and "postcard" has 1. No two values have the same number of occurrences.

# True
# Example 2 Explanation: The value "postcard" appears 4 times There's only one count (4), 
# which is technically unique, so this should also return True.

# False
# Example 3 Explanation: Each item appears 1 time All counts are 1, which is not unique, 
# so this should return False.


# Problem 3: Secret Beach
# You make friends with a local at your latest destination, and they give you a coded message with the name of a secret beach most tourists don't know about! You are given the strings key and message which represent a cipher key and a secret message, respectively. The steps to decode the message are as follows:

# Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
# Align the substitution table with the regular English alphabet.
# Each letter in message is then substituted using the table.
# Spaces ' ' are transformed to themselves.
# For example, given key = "travel the world" (an actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('t' -> 'a', 'r' -> 'b', 'a' -> 'c', 'v' -> 'd', 'e' -> 'e', 'l' -> 'f', 'h' -> 'g', 'w' -> 'h', 'o' -> 'i', 'd' -> 'j').

# Write a function decode_message() that accepts the strings key and message and returns a string representing the decoded message.

def decode_message(key, message):
    # create a substitution table
    substitution_table = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    used_chars = set()

    # loop through the key to create the table
    index = 0
    for char in key:
        if char.isalpha() and char not in used_chars:
            substitution_table[char] = alphabet[index] # add to table with corresponding letter from alphabet
            used_chars.add(char) # mark the char as used in the set
            index += 1
            if index == 26:
                break

    # decode the message
    decoded_message = []
    for char in message:
        if char == ' ':
            decoded_message.append(' ')
        else:
            decoded_message.append(substitution_table.get(char, char))

    return ''.join(decoded_message)


key1 = "the quick brown fox jumps over the lazy dog"
message1 = "vkbs bs t suepuv"

print(decode_message(key1, message1)) # Example Output 1: this is a secret

key2 = "eljuxhpwnyrdgtqkviszcfmabo"
message2 = "hntu depcte lxejw lxwntu zwx piqfx"

print(decode_message(key2, message2)) # Example Output 2: find laguna beach behind the grove



# Problem 4: Longest Harmonious Travel Sequence
# In a list of travel packages, we define a harmonious travel sequence as a sequence where the difference between the maximum and minimum travel ratings is exactly 1.

# Given an integer array rating, return the length of the longest harmonious travel sequence among all its possible subsequences.

# A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

# You are provided with a partially implemented solution that contains bugs. Your task is to identify and fix the bugs to ensure the solution works correctly.

def find_longest_harmonious_travel_sequence(ratings):
    # Initialize a dictionary to store the frequency of each rating
    frequency = {}

    # Count the occurrences of each rating
    for rating in ratings:
        if rating in frequency:
            frequency[rating] += 1 
        else:
            frequency[rating] = 1

    max_length = 0

    # Find the longest harmonious sequence
    for rating in frequency:
        if rating + 1 in frequency:
            max_length = max(max_length, frequency[rating] + frequency[rating + 1])  

    return max_length

durations1 = [1, 3, 2, 2, 5, 2, 3, 7]
durations2 = [1, 2, 3, 4]
durations3 = [1, 1, 1, 1]
durations4 = [1, 3, 2, 2, 5, 2, 3, 4, 6, 7, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 11]

print(find_longest_harmonious_travel_sequence(durations1)) # 5
print(find_longest_harmonious_travel_sequence(durations2)) # 2
print(find_longest_harmonious_travel_sequence(durations3)) # 0
print(find_longest_harmonious_travel_sequence(durations4)) # 10